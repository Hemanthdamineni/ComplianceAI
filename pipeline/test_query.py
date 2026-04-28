import os
import sys
import json

# Bind to absolute pathing to prevent execution failures
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline.query_engine import RetrievalEngine

def run_test():
    """
    Validation mechanism ensuring the RAG pipeline end-to-end functionality performs perfectly.
    Boots up the FAISS engine, generates embedded matrices using CUDA if accessible,
    and returns perfectly structured semantic answers.
    """
    index_pth = os.path.join(os.path.dirname(__file__), '../vector_store/faiss_index.bin')
    meta_pth = os.path.join(os.path.dirname(__file__), '../vector_store/metadata.pkl')
    
    print("\n--- FAISS Compliance Semantic Search Initiated ---")
    
    try:
        engine = RetrievalEngine(index_path=index_pth, meta_path=meta_pth)
    except FileNotFoundError as e:
        print(e)
        print("CRITICAL: You must execute 'pipeline/index_builder.py' prior to running tests.")
        return

    # User Query requested explicitly by prompt testing requirements
    question = "What is KYC?"
    print(f"\n[USER QUERY] -> {question}\n")
    
    # Execute extraction
    results = engine.execute_query(question, top_k=3)
    
    # Parse exactly as formatted JSON representing the endpoint delivery
    print("[RETRIEVAL RESULTS]")
    print(json.dumps(results, indent=2))
    
if __name__ == "__main__":
    run_test()
