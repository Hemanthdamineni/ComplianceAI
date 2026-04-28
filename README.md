# Compliance RAG Pipeline

A Retrieval-Augmented Generation (RAG) system that answers compliance questions (KYC, AML, audit) by semantically searching a curated corpus of internal policy documents, then grounding a **local LLM** (Llama 3.1 via Ollama) response in the retrieved evidence.

## Architecture

```
dataset/internal_docs/*.txt          ← structured chunked documents
        │
        ▼
pipeline/chunk_loader.py             ← parses chunks + JSON metadata
        │
        ▼
embeddings/embedder.py               ← sentence-transformers → float32 vectors
        │
        ▼
pipeline/index_builder.py            ← builds FAISS IndexFlatL2 + metadata pickle
        │
        ▼
vector_store/                        ← faiss_index.bin  +  metadata.pkl
        │
        ▼
pipeline/query_engine.py             ← embed query → FAISS search → rank → return
        │
        ▼
api/main.py                          ← FastAPI endpoint: /query  (POST)
                                       injects context into Ollama/Llama 3.1 prompt
```

## Quick Start

### Prerequisites

| Tool | Purpose |
|------|---------|
| [Pixi](https://pixi.sh) ≥ 0.66 | Reproducible environment manager |
| [Ollama](https://ollama.com) | Local LLM inference server |
| `ollama pull llama3.1:8b` | Pull the Llama 3.1 model |

### 1 — Install the environment

```bash
pixi install
```

This resolves **all** Python & native dependencies (PyTorch, FAISS, FastAPI, etc.) into an isolated `.pixi/` prefix.

### 2 — Build the FAISS index

```bash
pixi run build-index
```

Reads every `.txt` file under `dataset/internal_docs/`, generates embeddings via `all-MiniLM-L6-v2`, and writes `vector_store/faiss_index.bin` + `metadata.pkl`.

### 3 — Start the API server

```bash
# Make sure Ollama is running (it starts automatically on install)
pixi run serve
```

Launches uvicorn on `http://0.0.0.0:8000` with hot-reload.

### 4 — Query

```bash
curl -s http://localhost:8000/query \
  -H "Content-Type: application/json" \
  -d '{"question": "What is KYC?"}' | python -m json.tool
```

## Available Tasks

| Task | Command | Description |
|------|---------|-------------|
| **serve** | `pixi run serve` | Start FastAPI dev server (reload mode) |
| **build-index** | `pixi run build-index` | Rebuild FAISS index from document corpus |
| **test-query** | `pixi run test-query` | Run standalone retrieval smoke test |
| **gen-pdf** | `pixi run gen-pdf` | Convert internal `.txt` docs to PDF |

## Project Structure

```
.
├── api/
│   └── main.py              # FastAPI application + /query endpoint
├── dataset/
│   ├── internal_docs/        # 13 structured .txt compliance documents
│   ├── internal_docs_pdf/    # Generated PDFs
│   └── raw_pdfs/             # Source regulatory PDFs (RBI, SEBI)
├── embeddings/
│   └── embedder.py           # SentenceTransformer wrapper (CUDA-aware)
├── pipeline/
│   ├── chunk_loader.py       # Document parser (JSON metadata + text)
│   ├── index_builder.py      # FAISS index build pipeline
│   ├── query_engine.py       # Retrieval engine with scoring/ranking
│   └── test_query.py         # Standalone test harness
├── vector_store/
│   ├── faiss_index.bin        # Pre-built FAISS index
│   └── metadata.pkl           # Pickled chunk metadata
├── gen_pdf.py                 # Batch txt → PDF converter
├── pixi.toml                  # Pixi project manifest
└── README.md
```

## Key Dependencies

| Package | Role |
|---------|------|
| `sentence-transformers` | Embedding generation (`all-MiniLM-L6-v2`) |
| `faiss-cpu` | Flat L2 vector similarity search |
| `fastapi` + `uvicorn` | Async REST API |
| `openai` | OpenAI-compatible SDK (talking to local Ollama) |
| `fpdf2` | PDF generation from text docs |

## Environment Variables

## Local LLM (Ollama)

This project uses **Ollama** as the inference backend — no cloud API keys needed.

| Requirement | Command |
|-------------|--------|
| Install Ollama | `curl -fsSL https://ollama.com/install.sh \| sh` |
| Pull model | `ollama pull llama3.1:8b` |
| Verify running | `ollama list` |

The API server connects to Ollama at `http://localhost:11434` via the OpenAI-compatible endpoint.
