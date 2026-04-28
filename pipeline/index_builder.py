import os
import faiss
import pickle
import numpy as np
import sys

# Add parent directory for relative module imports
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from pipeline.chunk_loader import load_chunks
from embeddings.embedder import BackendEmbedder

def build_index(dataset_path: str, out_dir: str):
    """
    Operates the exact sequence defining Vector Pipeline Build:
    1. Loads physical chunks.
    2. Generates accelerated PyTorch embeddings.
    3. Pushes dimensions strictly into FAISS flat structure.
    4. Caches localized text metadata using Pickle. 
    """
    print("Initiating FAISS Index Build Pipeline...")
    
    # 1. Load Chunks
    chunks = load_chunks(dataset_path)
    if not chunks:
        print("Zero chunks detected. Halting pipeline.")
        return
    
    # 2. Extract payload for embeddings
    # We dynamically fuse embedded user queries with standard text payload to radically boost RAG hit accuracy
    texts_to_embed = []
    for chunk in chunks:
        metadata = chunk['metadata']
        queries = " ".join(metadata.get('user_queries', []))
        keywords = " ".join(metadata.get('keywords', []))
        raw_text = chunk['text']
        
        # Enriched string concatenating user_queries natively increases spatial proximity during exact FAISS search
        enriched_vector_string = f"{queries} {keywords} {raw_text}"
        texts_to_embed.append(enriched_vector_string)
        
    # 3. Request Embeddings
    embedder = BackendEmbedder()
    embeddings = embedder.get_embeddings(texts_to_embed)
    
    # FAISS expects float32 natively
    embeddings_f32 = np.array(embeddings).astype('float32')
    
    # 4. Synthesize FAISS index
    dimension = embeddings_f32.shape[1]
    index = faiss.IndexFlatL2(dimension)
    print(f"Configuring IndexFlatL2 with dimension {dimension}...")
    index.add(embeddings_f32)
    print(f"FAISS index loaded cleanly with {index.ntotal} distinct node vectors.")
    
    # 5. Commit output to disk
    if not os.path.exists(out_dir):
        os.makedirs(out_dir)
        
    faiss_path = os.path.join(out_dir, 'faiss_index.bin')
    meta_path = os.path.join(out_dir, 'metadata.pkl')
    
    faiss.write_index(index, faiss_path)
    with open(meta_path, 'wb') as f:
        pickle.dump(chunks, f)
        
    print(f"Artifact deployed successfully: {faiss_path}")
    print(f"Metadata securely cached: {meta_path}")

if __name__ == "__main__":
    docs_path = os.path.join(os.path.dirname(__file__), '../dataset/internal_docs')
    store_path = os.path.join(os.path.dirname(__file__), '../vector_store')
    build_index(docs_path, store_path)
