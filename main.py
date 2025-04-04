from dotenv import load_dotenv
load_dotenv()
import os

from langchain_google_genai import ChatGoogleGenerativeAI, GoogleGenerativeAIEmbeddings
from langchain_chroma import Chroma
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_core.prompts import ChatPromptTemplate

# Load environment variables
API_KEY = os.getenv('GEMINI_API_KEY')
DOC_PATH = os.getenv('DOC_PATH')
CHROMA_PATH = os.getenv('CHROMA_PATH')

if not all([API_KEY, DOC_PATH, CHROMA_PATH]):
    raise ValueError("Missing required environment variables. Please check your .env file")

# Initialize the LLM
llm = ChatGoogleGenerativeAI(model='gemini-2.5-pro-exp-03-25',api_key=API_KEY)

def loader(path):
    print(f"Loading document from: {path}")
    doc_loader = PyPDFLoader(path)
    documents = doc_loader.load()
    print(f"Loaded {len(documents)} pages")
    
    # Create text splitter with optimal parameters for PDFs
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=200,
        length_function=len,
        separators=["\n\n", "\n", " ", ""]
    )
    
    # Split documents into chunks
    chunks = text_splitter.split_documents(documents)
    print(f"Split into {len(chunks)} chunks")
    return chunks

def gen_data_store():
    documents = loader(DOC_PATH)
    
    # Initialize embedding function
    embedding_function = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=API_KEY
    )
    
    # Create and persist Chroma database
    print(f"Creating vector database at: {CHROMA_PATH}")
    db = Chroma.from_documents(
        documents=documents,
        embedding=embedding_function,
        persist_directory=CHROMA_PATH
    )
    print("Database created successfully")
    return db

prompt_content = """
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

def query(question):
    embedding_function = GoogleGenerativeAIEmbeddings(
        model="models/text-embedding-004",
        google_api_key=API_KEY
    )

    print("Loading vector database...")
    db = Chroma(persist_directory=CHROMA_PATH, embedding_function=embedding_function)
    
    print(f"Searching for: {question}")
    results = db.similarity_search_with_relevance_scores(question, k=4)

    if len(results) == 0:
        print("No results found in the document")
        return
    
    # Debug info
    print(f"Found {len(results)} results with scores: {[score for _, score in results]}")
    
    context_text = "\n\n---\n\n".join([doc.page_content for doc, _score in results])

    prompt_template = ChatPromptTemplate.from_template(prompt_content)
    chain = prompt_template | llm
    answer = chain.invoke({'context': context_text, 'question': question}).content
    sources = [doc.metadata.get("source", None) for doc, _score in results]

    return answer, sources

# Force regenerate the database
print("Initializing document database...")
gen_data_store()

# Test query
question = 'Which test sets were used to sample the source sentences for the Chinese to English and English to Russian tasks?'
print("\nTesting query system...")
result = query(question)
if result:
    response, source = result
    print("\nResponse:", response)
    print("Source:", source)
else:
    print("No response")