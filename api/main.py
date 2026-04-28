import os
import sys
from contextlib import asynccontextmanager

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import FileResponse
from fastapi.staticfiles import StaticFiles
from pydantic import BaseModel
from openai import OpenAI

# Crucial setup to allow importing the internal RAG pipeline modules
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))
from pipeline.query_engine import RetrievalEngine

# Global placeholder for the memory-heavy FAISS engine
engine = None

@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Ensures the FAISS index and the sentence-transformer models are loaded into 
    GPU/RAM strictly ONCE during startup, drastically optimizing query latency.
    """
    global engine
    print("Booting up Compliance AI System...")
    
    index_pth = os.path.join(os.path.dirname(__file__), '../vector_store/faiss_index.bin')
    meta_pth = os.path.join(os.path.dirname(__file__), '../vector_store/metadata.pkl')
    
    engine = RetrievalEngine(index_path=index_pth, meta_path=meta_pth)
    print("FAISS Retrieval Engine initialized globally. API Ready for requests.")
    yield
    # Actions executed on shutdown
    print("Compliance AI API shutting down...")

# Initialize FastAPI app with lifespan manager
app = FastAPI(title="Compliance RAG API", lifespan=lifespan)

# Initialize OpenAI-compatible client pointed at the local Ollama server
client = OpenAI(
    base_url="http://localhost:11434/v1",
    api_key="ollama",  # Ollama doesn't validate API keys; this is a required placeholder
)

# Inject CORS parameters allowing unhindered frontend connectivity
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- Pydantic Data Schemas ---

class QueryRequest(BaseModel):
    question: str

# --- Endpoints ---

@app.get("/")
def serve_ui():
    """
    Serves the ComplianceAI SPA frontend.
    """
    ui_path = os.path.join(os.path.dirname(__file__), '../ui/index.html')
    return FileResponse(ui_path, media_type='text/html')


@app.get("/health")
def health_check():
    """
    Standard heartbeat ping to verify API operational status.
    """
    return "Compliance AI API Running"


@app.post("/query")
def execute_rag_query(request: QueryRequest):
    """
    Primary RAG interface. Pushes a natural language string through the global FAISS engine,
    formats top 3 results into a context, and uses OpenAI to generate a grounded answer.
    """
    if engine is None:
        return {
            "answer": "System offline or FAISS index missing.",
            "sources": []
        }
        
    # Execute extraction for top 3 chunks
    raw_results = engine.execute_query(request.question, top_k=3)
    
    if not raw_results:
        return {
            "answer": "No relevant institutional documents found regarding this query.",
            "sources": []
        }
        
    context_parts = []
    sources = []
    for i, chunk in enumerate(raw_results, 1):
        context_parts.append(f"<chunk{i} DIRECT_ANSWER: {chunk['answer']}\n{chunk['text']}>")
        sources.append({
            "chunk_id": chunk["chunk_id"],
            "citation": chunk["source"]
        })
        
    context = "\n\n".join(context_parts)
    
    prompt = f"""You are a compliance assistant.

Answer ONLY using the provided context.
Do not add external knowledge.
If answer is not in context, say 'Not found in compliance documents'.

Question: {request.question}

Context:
{context}
"""

    try:
        response = client.chat.completions.create(
            model="llama3.1:8b",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.0
        )
        llm_answer = response.choices[0].message.content
    except Exception as e:
        llm_answer = f"Error generating answer: {str(e)}"
        
    return {
        "answer": llm_answer,
        "sources": sources
    }
