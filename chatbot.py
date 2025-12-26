import os
from langchain_ollama import OllamaLLM
from vector_store import VectorManager

class LocalAIChatbot:
    def __init__(self):
        # 1. Connect to My Vector Store on H: drive
        self.v_db = VectorManager()
        
        # 2. Initialize the Local Librarian (Ollama)
        self.model = OllamaLLM(model="llama3")

    def ask(self, question):
        # --- ALL THIS CODE MUST BE INDENTED ONE TAB TO THE RIGHT ---
        # 1. Retrieve the data from My H: drive
        context_chunks = self.v_db.search_relevant_context(question, top_n=3)
        
        # --- DEBUGGING LINE ---
        print(f"📄 DEBUG: Found {len(context_chunks)} matching pieces of info in My files.")
        for i, chunk in enumerate(context_chunks):
            print(f"   Chunk {i+1}: {chunk[:100]}...") 
        # ----------------------

        context_text = "\n".join(context_chunks)

        # 2. Update the Prompt to be very strict
        prompt = f"""
        You are a strict assistant. Answer the question using ONLY the context provided below.
        If the context does not contain the answer, say "I cannot find this in the documents."
        
        CONTEXT:
        {context_text}
        
        QUESTION: {question}
        
        ANSWER:
        """

        response = self.model.invoke(prompt)
        return response

if __name__ == "__main__":
    bot = LocalAIChatbot()
    print("🚀 Local RAG Online (No Quotas!). Type 'exit' to stop.")
    
    while True:
        query = input("\n👤 You: ")
        if query.lower() in ['exit', 'quit']:
            break
            
        answer = bot.ask(query)
        print(f"\n🤖 AI: {answer}") 