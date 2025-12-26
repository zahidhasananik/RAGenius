import chromadb
from langchain_community.embeddings import SentenceTransformerEmbeddings

class VectorManager:
    def __init__(self, database_path="./chroma_db"):
        # 1. Initialize the Embedding Model (This runs locally on your CPU/GPU)
        self.model = SentenceTransformerEmbeddings(model_name="all-MiniLM-L6-v2")
        
        # 2. Connect to ChromaDB on your H: drive
        self.client = chromadb.PersistentClient(path=database_path)
        
        # 3. Create or get a collection (Think of this as a table in a database)
        self.collection = self.client.get_or_create_collection(name="company_knowledge_base")

    def add_chunks_to_db(self, chunks):
        """Converts chunks to vectors and saves them."""
        ids = [f"chunk_{i}" for i in range(len(chunks))]
        
        self.collection.add(
            documents=chunks,
            ids=ids
        )
        print(f"✅ Added {len(chunks)} chunks to the vector database.")

    def search_relevant_context(self, query, top_n=3):
        """Searches the database for the most relevant text."""
        results = self.collection.query(
            query_texts=[query],
            n_results=top_n
        )
        return results['documents'][0]

# --- Quick Test ---
if __name__ == "__main__":
    vm = VectorManager()
    # Example chunks (In reality, these come from your ingestion.py)
    sample_chunks = [
        "Apex DMIT provides 24/7 data management services.",
        "The company is based in the US and Bangladesh.",
        "AI engineers at Apex focus on financial sector solutions."
    ]
    
    vm.add_chunks_to_db(sample_chunks)
    
    # Try a search
    query = "Where is the company located?"
    context = vm.search_relevant_context(query)
    print(f"🔍 Search Result: {context}")