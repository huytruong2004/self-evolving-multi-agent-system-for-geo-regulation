import os
from typing import List, Dict, Literal
import chromadb
from dotenv import load_dotenv

from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_core.documents import Document
from langchain_chroma import Chroma
from langchain_community.retrievers import BM25Retriever
from langchain.retrievers import EnsembleRetriever

# Load environment variables
load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/embedding-001",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# Load all documents from ChromaDB for both retrievers
client = chromadb.PersistentClient(path="./chroma_db")
collection = client.get_collection("semantic_chunks_gradient_05")

print("Loading documents for hybrid search...")
all_results = collection.get(include=['documents', 'metadatas'])
documents = []

for i, doc in enumerate(all_results['documents']):
    metadata = all_results['metadatas'][i] if all_results['metadatas'] else {}
    documents.append(Document(
        page_content=doc,
        metadata=metadata or {}
    ))

# Create vector store retriever
vectorstore = Chroma.from_documents(documents, embeddings)
vectorstore_retriever = vectorstore.as_retriever(search_kwargs={"k": 5})

# Create keyword retriever
keyword_retriever = BM25Retriever.from_documents(documents)
keyword_retriever.k = 5

# Create ensemble (hybrid) retriever
ensemble_retriever = EnsembleRetriever(
    retrievers=[vectorstore_retriever, keyword_retriever],
    weights=[0.7, 0.3]  # 70% semantic, 30% keyword
)

print(f"Loaded {len(documents)} documents for hybrid search")

def vector_search(query: str, n_results: int = 10) -> List[Dict]:
    """
    Minimal search function for ChromaDB collection.
    Args:
        query (str): The search query.
        n_results (int, optional): The number of results to return. Defaults to 5.
    Returns:
        List[Dict]: A list of search results, each containing:
            - content (str): The content of the chunk.
            - distance (float): The distance score of the chunk.
            - source (str): The source file of the chunk.
            - json_file (str): The JSON file associated with the chunk.
    """
    search_type = "hybrid"  # Change this to "semantic", "keyword", or "hybrid"
    # Set the number of results for all retrievers
    vectorstore_retriever.search_kwargs["k"] = n_results
    keyword_retriever.k = n_results
    
    # Choose retriever based on search type
    if search_type == "semantic":
        retriever = vectorstore_retriever
    elif search_type == "keyword":
        retriever = keyword_retriever
    else:  # hybrid
        retriever = ensemble_retriever
    
    # Get results
    results = retriever.get_relevant_documents(query)
    
    # Format results
    search_results = []
    for i, doc in enumerate(results[:n_results]):
        search_results.append({
            'content': doc.page_content,
            'source': doc.metadata.get('source_file', 'Unknown'),
            'json_file': doc.metadata.get('json_file', 'Unknown'),
            'search_type': search_type,
            'rank': i + 1
        })
    
    return search_results