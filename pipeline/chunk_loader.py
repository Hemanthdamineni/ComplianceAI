import os
import re
import json
from typing import List, Dict, Any

def load_chunks(docs_dir: str = '../dataset/internal_docs') -> List[Dict[str, Any]]:
    """
    Reads all .txt files from the specified directory and extracts structured chunks.
    Assumes chunks are separated by '---' and contain a JSON metadata block at the top.
    """
    chunks = []
    if not os.path.exists(docs_dir):
        print(f"Directory {docs_dir} not found.")
        return chunks

    for filename in os.listdir(docs_dir):
        if not filename.endswith('.txt'):
            continue
        
        filepath = os.path.join(docs_dir, filename)
        with open(filepath, 'r', encoding='utf-8') as f:
            content = f.read()

        # Files are separated by '---'
        raw_chunks = re.split(r'\n\s*---\s*\n', content)

        for raw_chunk in raw_chunks:
            raw_chunk = raw_chunk.strip()
            if not raw_chunk:
                continue
            
            # Extract JSON metadata which is at the start of the chunk
            json_match = re.search(r'(\{.*?\})', raw_chunk, re.DOTALL)
            if not json_match:
                continue
            
            try:
                metadata = json.loads(json_match.group(1))
            except json.JSONDecodeError as e:
                print(f"Failed to parse JSON in {filename}: {e}")
                continue
            
            chunk_id = metadata.get("chunk_id", "UNKNOWN")
            
            # The actual content starts after the JSON block
            text_block = raw_chunk[json_match.end():].strip()

            chunks.append({
                "chunk_id": chunk_id,
                "text": text_block,
                "metadata": metadata
            })
            
    print(f"Loaded {len(chunks)} chunks from {docs_dir}.")
    return chunks

if __name__ == "__main__":
    # Test execution
    res = load_chunks()
    if res:
        print(f"Sample chunk: {res[0]['chunk_id']}")
