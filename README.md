# 🚀 Enterprise RAG Assistant

A production-grade **Retrieval-Augmented Generation (RAG)** backend built from scratch using **FastAPI**, **OpenAI GPT**, **Sentence Transformers**, and **Qdrant**.

This project demonstrates the complete lifecycle of a modern RAG system—from document ingestion and semantic indexing to vector retrieval and LLM-powered answer generation.

---

## ✨ Features

- 📄 **Multi-Format Document Ingestion:** Supports `PDF`, `DOCX`, and `TXT` files.
- ✂️ **Recursive Text Chunking:** Smart chunking with configurable overlap to preserve context.
- 🧠 **Semantic Embeddings:** High-performance dense embeddings via Sentence Transformers.
- 🗂 **Persistent Vector Storage:** Vector similarity search powered by Qdrant.
- 🔍 **Semantic Similarity Search:** Top-K relevant context retrieval for precise prompting.
- 🤖 **OpenAI GPT Integration:** Dynamic contextualized response synthesis.
- ⚡ **FastAPI REST APIs:** Asynchronous, non-blocking HTTP endpoints.
- ⚙️ **Environment-Based Configuration:** Built using `pydantic-settings`.
- 📝 **Structured Logging:** Centralized logging for debugging and monitoring.
- 📦 **Modular Architecture:** Clean separation of concerns across service layers.

---

# 🏗️ Architecture

```text
                    INDEXING PIPELINE

        PDF / DOCX / TXT
                │
                ▼
        Document Loader
                │
                ▼
        Document Object
                │
                ▼
      Recursive Chunking
                │
                ▼
   Sentence Transformer Embeddings
                │
                ▼
      Qdrant Vector Database


                    QUERY PIPELINE

          User Question
                │
                ▼
        Query Embedding
                │
                ▼
      Semantic Retrieval
                │
                ▼
      Top-K Relevant Chunks
                │
                ▼
        Prompt Builder
                │
                ▼
        OpenAI GPT Model
                │
                ▼
          Final Response
```

---

# 🧩 Project Structure

```text
enterprise-rag-assistant/
├── app/
│   ├── api/
│   │   └── v1/
│   │       ├── chat.py
│   │       ├── health.py
│   │       ├── upload.py
│   │       └── router.py
│   ├── core/
│   │   ├── config.py
│   │   ├── logger.py
│   │   ├── exceptions.py
│   │   └── lifespan.py
│   ├── embeddings/
│   ├── ingestion/
│   ├── llm/
│   ├── processing/
│   ├── retrieval/
│   ├── schemas/
│   ├── services/
│   └── vectorstore/
├── data/
├── logs/
├── tests/
├── main.py
├── requirements.txt
├── Dockerfile
├── docker-compose.yml
└── README.md
```

---

# ⚙️ Tech Stack

| Category          | Technology                   |
| ----------------- | ---------------------------- |
| Backend Framework | FastAPI                      |
| Language          | Python 3.10+                 |
| LLM Provider      | OpenAI GPT-4.1-mini / GPT-4o |
| Embedding Model   | all-MiniLM-L6-v2             |
| Vector Database   | Qdrant                       |
| PDF Parsing       | PyMuPDF (fitz)               |
| DOCX Parsing      | python-docx                  |
| Text Chunking     | LangChain Text Splitters     |
| Validation        | Pydantic v2                  |

---

# 🔄 End-to-End Workflow

```text
                    DOCUMENT INDEXING

Document
    │
    ▼
Document Loader
    │
    ▼
Document Object
    │
    ▼
Recursive Chunking
    │
    ▼
Text Chunks
    │
    ▼
Embedding Model
    │
    ▼
Vector Embeddings
    │
    ▼
Qdrant


───────────────────────────────────────────────────────────────────────────────

                    QUESTION ANSWERING

User Question
    │
    ▼
Query Embedding
    │
    ▼
Vector Similarity Search
    │
    ▼
Top-K Relevant Chunks
    │
    ▼
Prompt Construction
    │
    ▼
OpenAI GPT
    │
    ▼
Final Answer
```

---

# 🌐 REST API Specifications

## 1. Health Check

### Endpoint

```http
GET /api/v1/health
```

### Response

```json
{
  "status": "healthy"
}
```

---

## 2. Upload & Index Document

### Endpoint

```http
POST /api/v1/upload
```

**Content-Type**

```text
multipart/form-data
```

**Supported File Types**

- PDF
- DOCX
- TXT

### Response

```json
{
  "success": true,
  "filename": "BackendResume.pdf",
  "message": "Document uploaded and indexed successfully."
}
```

---

## 3. Contextual Chat Query

### Endpoint

```http
POST /api/v1/chat
```

### Request

```json
{
  "question": "What backend projects has Chandra Sekhar built?"
}
```

### Response

```json
{
  "answer": "Chandra Sekhar built the Enterprise RAG Assistant backend using FastAPI and Qdrant...",
  "sources": ["BackendResume.pdf"]
}
```

---

# 🚀 Quickstart & Installation

## Prerequisites

- Python 3.10+
- Docker Desktop

---

## 1. Clone the Repository

```bash
git clone https://github.com/chandrasekharaila/enterprise-rag-assistant.git

cd enterprise-rag-assistant

python -m venv venv
```

### Mac/Linux

```bash
source venv/bin/activate
```

### Windows

```bash
venv\Scripts\activate
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

---

## 2. Configure Environment Variables

Create a `.env` file in the project root.

```env
OPENAI_API_KEY=your_openai_api_key_here

LLM_MODEL=gpt-4.1-mini

EMBEDDING_MODEL=all-MiniLM-L6-v2

QDRANT_HOST=localhost
QDRANT_PORT=6333
QDRANT_COLLECTION=enterprise_rag

CHUNK_SIZE=500
CHUNK_OVERLAP=100

TEMPERATURE=0.2
MAX_TOKENS=1000
```

---

## 3. Start Qdrant

```bash
docker run -d \
  --name qdrant \
  -p 6333:6333 \
  -p 6334:6334 \
  -v "$(pwd)/qdrant_storage:/qdrant/storage:z" \
  qdrant/qdrant
```

Or simply use Docker Compose:

```bash
docker compose up -d
```

### Useful URLs

| Service          | URL                             |
| ---------------- | ------------------------------- |
| Qdrant Dashboard | http://localhost:6333/dashboard |
| REST API         | http://localhost:6333           |
| gRPC             | localhost:6334                  |

---

## 4. Run FastAPI

```bash
uvicorn main:app --reload
```

### API Documentation

Swagger UI

```
http://localhost:8000/docs
```

ReDoc

```
http://localhost:8000/redoc
```

---

# 💡 Key Learnings

### End-to-End RAG Architecture

Built a modular ingestion and retrieval pipeline without relying on high-level abstraction frameworks, gaining a deeper understanding of how modern RAG systems work internally.

### Vector Database Integration

Integrated Qdrant for semantic search, implemented persistent storage, and handled database lifecycle management using Docker and FastAPI.

### Chunking Strategies

Applied recursive text chunking with contextual overlap to improve retrieval quality and preserve semantic meaning during embedding generation.

### Production Backend Practices

Designed a modular backend using FastAPI, Pydantic v2, structured logging, dependency injection, and clean service-layer architecture.

---

# 🔮 Future Improvements

- [ ] Hybrid Search (Dense + BM25)
- [ ] Conversation Memory
- [ ] RAG Evaluation using RAGAS
- [ ] Streaming Responses (SSE/WebSockets)
- [ ] Metadata Filtering
- [ ] Authentication & Multi-user Support
- [ ] Docker Deployment to Cloud
- [ ] CI/CD Pipeline with GitHub Actions

---

# 👨‍💻 Author

**Chandra Sekhar**

- GitHub: https://github.com/chandrasekharaila
- LinkedIn: https://linkedin.com/in/chandrasekharaila

---

## ⭐ Support

If you found this project helpful, consider giving the repository a ⭐ on GitHub.
