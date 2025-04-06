"""Query handling and response generation."""
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.prompts import ChatPromptTemplate

from src.config.settings import API_KEY, GEMINI_MODEL
from src.database.document_store import get_database

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model=GEMINI_MODEL, api_key=API_KEY)

PROMPT_TEMPLATE = """
Role:
    You are a document insights provider. Your task is to generate well-structured responses using tables, bullet points, 
    or well-formatted paragraphs when appropriate.

Guidelines:
    - Use only the provided document as the source of truth.
    - Do not generate information beyond the given context (avoid hallucinations).
    - Ensure responses are clear, structured, and directly relevant to the question.

Input:
    - Context: {context}
    - Question: {question}

Output Format:
    Provide a response that is:
        - Concise yet informative.
        - Properly structured (e.g., tables, bullet points, or paragraphs based on content type).
        - Strictly based on the given document.
"""

def query_document(question):
    """Query the document and generate a response."""
    db = get_database()
    
    print(f"Searching for: {question}")
    results = db.similarity_search_with_relevance_scores(question, k=4)

    if len(results) == 0:
        print("No results found in the document")
        return "I couldn't find any relevant information in the document to answer your question."
    
    print(f"Found {len(results)} results with scores: {[score for _, score in results]}")
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])
    prompt_template = ChatPromptTemplate.from_template(PROMPT_TEMPLATE)
    chain = prompt_template | llm
    
    return chain.invoke({'context': context_text, 'question': question}).content

def chat_response(message, history):
    """Handle chat messages and maintain conversation history."""
    return query_document(message)
