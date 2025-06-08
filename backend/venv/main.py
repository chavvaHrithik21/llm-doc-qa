from fastapi import FastAPI, UploadFile, File, Form
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
from qa_pipeline import process_pdf, get_answer
import os

load_dotenv()
app = FastAPI()

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        return {"error": "Only PDF files are supported."}
    try:
        content = await file.read()
        process_pdf(content)
        return {"message": "Document processed successfully."}
    except Exception as e:
        return {"error": str(e)}

@app.post("/query")
async def query_doc(question: str = Form(...)):
    try:
        answer = get_answer(question)
        return {"answer": answer}
    except Exception as e:
        return {"error": str(e)}
