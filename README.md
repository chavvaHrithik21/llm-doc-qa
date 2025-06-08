# llm-doc-qa
LLM-powered document Q&amp;A system using FastAPI, HuggingFace Transformers, and Chroma.

# LLM Document Q&A System

A lightweight, local-first document question answering system built with:
- `FastAPI` for the backend
- `HuggingFace Transformers` (using `flan-t5-base`)
- `LangChain` with `Chroma` as the vector store
- `Next.js` (planned) for the frontend

### Features
- Upload PDF files
- Query documents using natural language
- No OpenAI API required – runs on CPU
- Embeddings: `all-MiniLM-L6-v2`
- Planned integrations: S3, MLflow, and citations

---

> Built and maintained by [@hrithikchavva](https://github.com/hrithikchavva)
