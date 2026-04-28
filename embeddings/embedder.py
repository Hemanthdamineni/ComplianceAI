import torch
from sentence_transformers import SentenceTransformer
from typing import List
import numpy as np

class BackendEmbedder:
    def __init__(self, model_name: str = "all-MiniLM-L6-v2"):
        """
        Initializes the sentence transformer model and automatically maps to GPU if CUDA is available.
        Ensures no hardcoded CPU mapping.
        """
        self.device = "cuda" if torch.cuda.is_available() else "cpu"
        print(f"Loading SentenceTransformer model '{model_name}' on device: {self.device}...")
        self.model = SentenceTransformer(model_name, device=self.device)

    def get_embeddings(self, texts: List[str]) -> np.ndarray:
        """
        Convert a list of text strings into uniform dimensional embeddings using PyTorch.
        Returns the vectors as a float32 NumPy array ready for FAISS ingestion.
        """
        # encode() operates out-of-the-box with CUDA batching capabilities
        embeddings = self.model.encode(texts, convert_to_numpy=True, show_progress_bar=True)
        return embeddings

if __name__ == "__main__":
    # Standard standalone module test
    embedder = BackendEmbedder()
    test_emb = embedder.get_embeddings(["What is KYC?", "What is AML?"])
    print(f"Embedding batch generated beautifully. Matrix Shape: {test_emb.shape}")
