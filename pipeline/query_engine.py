import os
import faiss
import pickle
import numpy as np
import sys
import re
from typing import List, Dict, Any

# Ensure parent directory is traversable for relative importing
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from embeddings.embedder import BackendEmbedder

class RetrievalEngine:
    def __init__(self, index_path: str = '../vector_store/faiss_index.bin', meta_path: str = '../vector_store/metadata.pkl'):
        """
        Dynamically initializes the Query Engine by parsing the precompiled FAISS L2 flat array
        and binding it to the cached Python metadata definitions.
        """
        if not os.path.exists(index_path) or not os.path.exists(meta_path):
            raise FileNotFoundError(f"Missing pipeline dependencies! Ensure {index_path} and {meta_path} are generated.")
            
        print(f"Loading FAISS Index from {index_path}...")
        self.index = faiss.read_index(index_path)
        
        with open(meta_path, 'rb') as f:
            self.metadata_store = pickle.load(f)
            
        # Instantiate embedder. It will securely fallback to CUDA if available automatically.
        self.embedder = BackendEmbedder()
        print(f"Retrieval Engine online. Managing {self.index.ntotal} vectors.")

    def _extract_direct_answer(self, raw_text: str) -> str:
        """
        Helper method traversing the raw unstructured chunk layout aiming distinctly 
        to strip out the pre-baked DIRECT_ANSWER payload natively stored in the block.
        """
        match = re.search(r'DIRECT_ANSWER:\s*(.*?)\n\s*(?:SEARCH_TERMS:|REGULATION SOURCE:)', raw_text, re.DOTALL | re.IGNORECASE)
        if match:
            return match.group(1).strip()
        return "Direct answer unavailable within specific chunk geometry."

    def execute_query(self, query: str, top_k: int = 5) -> List[Dict[str, str]]:
        """
        Pushes a natural language string through the PyTorch embedder and natively 
        queries FAISS for mathematical proximity matches.
        """
        # Embed the query
        query_vectors = self.embedder.get_embeddings([query])
        query_vector = np.array(query_vectors).astype('float32')
        
        # Execute rapid FAISS proximity sweep
        # We fetch an expanded pool to allow rigorous downstream filtering
        fetch_k = max(10, top_k * 2) 
        distances, indices = self.index.search(query_vector, k=fetch_k)
        
        # Identify if the user is seeking a definition
        def_keywords = ["what is", "define", "meaning"]
        is_def_query = any(k in query.lower() for k in def_keywords)
        
        raw_results = []
        for i in range(fetch_k):
            idx = indices[0][i]
            if idx == -1:
                continue
                
            dist = float(distances[0][i])
            
            # Score threshold filtering: Remove distant vectors
            if dist >= 1.2:
                continue
                
            chunk_data = self.metadata_store[idx]
            chunk_id = chunk_data.get('chunk_id', 'UNKNOWN_ID')
            source_file = chunk_data.get('metadata', {}).get('source_file_path', 'Unknown file')
            
            direct_ans = self._extract_direct_answer(chunk_data['text'])
            
            # Noise Removal: Drop irrelevant procedural chunks for pure definition queries
            if is_def_query:
                noisy_terms = ["audit_guidelines", "periodic_updation"]
                if any(n in source_file.lower() for n in noisy_terms):
                    continue
            
            raw_results.append({
                "chunk_id": chunk_id,
                "answer": direct_ans,
                "text": chunk_data.get('text', ''),
                "source": source_file,
                "raw_score": dist
            })
            
        # Advanced Sorting Algorithm
        def ranker(item):
            score = item["raw_score"]
            is_def_file = "definitions.txt" in item["source"].lower()
            has_ans = item["answer"] != "Direct answer unavailable within specific chunk geometry."
            
            # Prioritize chunks possessing a DIRECT_ANSWER parameter
            if not has_ans:
                score += 500.0
                
            # Heavily prioritize definitions.txt chunks for definition-oriented queries
            if is_def_query and is_def_file:
                score -= 1000.0  
                
            return score
            
        sorted_results = sorted(raw_results, key=ranker)
        
        # Final formatting: Slice to Top 2-3 most relevant hits based on requested top_k bound
        final_k = min(3, top_k)
        
        final_results = []
        for r in sorted_results[:final_k]:
            final_results.append({
                "chunk_id": r["chunk_id"],
                "answer": r["answer"],
                "text": r["text"],
                "source": r["source"],
                "score": f"{r['raw_score']:.4f}"
            })
            
        return final_results

if __name__ == "__main__":
    # Test script directly within the module
    engine = RetrievalEngine(
        index_path=os.path.join(os.path.dirname(__file__), '../vector_store/faiss_index.bin'),
        meta_path=os.path.join(os.path.dirname(__file__), '../vector_store/metadata.pkl')
    )
    test_result = engine.execute_query("What happens if a customer ignores KYC updation?", top_k=2)
    print(test_result)
