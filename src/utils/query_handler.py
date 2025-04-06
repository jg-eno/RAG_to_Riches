"""Query handling and response generation."""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from functools import lru_cache
import time
import os
from google.api_core.exceptions import ResourceExhausted
from langchain_groq import ChatGroq

from src.config.settings import API_KEY, GEMINI_MODEL
from src.database.document_store import get_database

# Initialize the Google Gemini LLM (now used as fallback)
def get_gemini_llm():
    """Get a new Google Gemini LLM instance with the next API key."""
    return ChatGoogleGenerativeAI(
        model=GEMINI_MODEL, 
        api_key=API_KEY(),  # Call the function to get the next API key
        temperature=0.3,  # Lower temperature for faster, more deterministic responses
        max_output_tokens=1024,  # Limit output tokens for faster generation
        top_p=0.95,  # Slightly reduce top_p for faster generation
        top_k=40,  # Set top_k for better performance
    )

# Initialize the Groq LLM as primary
def get_groq_llm():
    """Get a Groq LLM instance as the primary LLM."""
    groq_api_key = os.getenv("GROQ_API_KEY")
    if not groq_api_key:
        raise ValueError("GROQ_API_KEY not found in environment variables")
    
    return ChatGroq(
        model="llama-3.3-70b-specdec",
        api_key=groq_api_key,
        temperature=0.3,
        max_tokens=1024,
        model_kwargs={"top_p": 0.95},  # Pass top_p through model_kwargs instead
    )

# Create a reusable chain with output parser
output_parser = StrOutputParser()

PROMPT_TEMPLATE = """
Role:
    You are a document insights provider. Your task is to generate well-structured responses using tables, bullet points, 
    or well-formatted paragraphs when appropriate.

Guidelines:
    - Use only the provided document as the source of truth.
    - Do not generate information beyond the given context (avoid hallucinations).
    - Ensure responses are clear, structured, and directly relevant to the question.
    - Use Markdown formatting for better presentation:
        * Create tables with proper headers and alignment
        * Use bullet points and numbered lists where appropriate
        * Use headings (##, ###) to organize longer responses
        * Bold important terms or findings
        * Use code blocks for any technical content
    - Be concise and focused - prioritize relevant information only.

Input:
    - Context: {context}
    - Question: {question}

Output Format:
    Provide a response that is:
        - Concise yet informative.
        - Properly structured (e.g., tables, bullet points, or paragraphs based on content type).
        - Strictly based on the given document.
        - Well-formatted with Markdown for readability.
"""

@lru_cache(maxsize=5)  # Cache the 5 most recent chain configurations
def get_chain(use_fallback=False):
    """Get the LLM chain with caching.
    
    Args:
        use_fallback: Whether to use the fallback Google Gemini LLM instead of Groq
    """
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    
    if use_fallback:
        print("Using Google Gemini LLM as fallback")
        return prompt_template | get_gemini_llm() | output_parser
    else:
        print("Using Groq LLM as primary")
        return prompt_template | get_groq_llm() | output_parser

# Cache for storing query results to avoid redundant processing
query_cache = {}

def query_document(question, doc_path=None):
    """Query the document and generate a response with caching."""
    # Create a cache key that includes both the question and document path
    cache_key = f"{doc_path}:{question}" if doc_path else question
    
    if cache_key in query_cache:
        print(f"Cache hit for question: {question}")
        return query_cache[cache_key]
    
    start_time = time.time()
    db = get_database(doc_path)
    
    print(f"Searching for: {question} in document: {doc_path}")
    results = db.similarity_search_with_relevance_scores(
        question, 
        k=3
    )

    # Handle negative relevance scores by using absolute values
    if results and all(score < 0 for _, score in results):
        print("Detected negative relevance scores, using absolute values for comparison")
        # Sort by absolute value of relevance score (closest to 0 is most relevant for negative scores)
        results.sort(key=lambda x: abs(x[1]))
        
    if len(results) == 0:
        print("No results found in the document")
        return "I couldn't find any relevant information in the document to answer your question."
    
    print(f"Found {len(results)} results with scores: {[score for _, score in results]}")
    retrieval_time = time.time() - start_time
    print(f"Retrieval completed in {retrieval_time:.2f} seconds")
    
    # Sort by relevance and join the most relevant chunks
    results.sort(key=lambda x: x[1], reverse=True)
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    
    # Try with primary Groq LLM first, fall back to Google Gemini if there's an error
    try:
        chain = get_chain(use_fallback=False)
        generation_start = time.time()
        response = chain.invoke({'context': context_text, 'question': question})
        generation_time = time.time() - generation_start
        print(f"Response generation completed in {generation_time:.2f} seconds")
    except Exception as e:
        print(f"Groq API error: {str(e)}")
        print("Falling back to Google Gemini LLM...")
        
        try:
            # Use Google Gemini as fallback
            chain = get_chain(use_fallback=True)
            generation_start = time.time()
            response = chain.invoke({'context': context_text, 'question': question})
            generation_time = time.time() - generation_start
            print(f"Fallback response generation completed in {generation_time:.2f} seconds")
        except ResourceExhausted as fallback_error:
            print(f"Google API quota exceeded: {str(fallback_error)}")
            return "I'm sorry, but I'm currently experiencing technical difficulties with both primary and fallback language models. Please try again later."
        except Exception as fallback_error:
            print(f"Fallback LLM also failed: {str(fallback_error)}")
            return "I'm sorry, but I'm currently experiencing technical difficulties with both primary and fallback language models. Please try again later."
    
    # Cache the result
    query_cache[cache_key] = response
    
    total_time = time.time() - start_time
    print(f"Total query processing time: {total_time:.2f} seconds")
    
    return response

def chat_response(message, history, active_document=None):
    """Handle chat messages and maintain conversation history."""
    answer = query_document(message, active_document)
    
    return "", history + [
        {"role": "user", "content": message},
        {"role": "assistant", "content": answer}
    ]
