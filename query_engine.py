import chromadb
from langchain_community.embeddings import SentenceTransformerEmbeddings

def query_docs(user_question):
    # 1. Load the same embedding model
    embeddings = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")

    # 2. Connect to My existing database on H: drive
    client = chromadb.PersistentClient(path="./chroma_db")
    collection = client.get_collection(name="my_documents")

    # 3. Search the database
    # It converts the question to a vector and finds the "closest" text chunks
    results = collection.query(
        query_embeddings=[embeddings.embed_query(user_question)],
        n_results=2  # Give me the top 2 most relevant chunks
    )

    return results['documents']

# --- Quick Test ---
if __name__ == "__main__":
    question = "What is the main topic of the document?"
    answers = query_docs(question)
    print(f"Top Result: {answers[0]}")