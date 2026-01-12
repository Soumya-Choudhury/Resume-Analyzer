from fastapi import APIRouter, UploadFile, File, Form, HTTPException
from pypdf import PdfReader
from langchain_core.messages import HumanMessage
import json
import re
import traceback
from rag.llm import get_llm
from rag.embeddings import get_embeddings
from rag.splitter import split_text
from rag.vector_store import build_vector_store

router = APIRouter(prefix="/api", tags=["Resume Analyzer"])

def extract_text_from_pdf(file: UploadFile) -> str:
    reader = PdfReader(file.file)
    text = ""
    for page in reader.pages:
        text += page.extract_text() or ""
    return text.strip()


def extract_json(text: str) -> dict:
    """
    Extract first valid JSON object from LLM output
    """
    match = re.search(r"\{[\s\S]*\}", text)
    if not match:
        raise ValueError("No JSON found in model output")
    return json.loads(match.group())


# ------------------ Route ------------------

@router.post("/analyze")
async def analyze_resume(
    resume: UploadFile = File(...),
    jd: str = Form(...)
):
    print("Received request")
    # Validate input
    if not resume.filename.lower().endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Resume must be a PDF")

    if not jd.strip():
        raise HTTPException(status_code=400, detail="Job description is empty")

    # Extract resume text
    resume_text = extract_text_from_pdf(resume)
    if not resume_text.strip():
        raise HTTPException(
        status_code=400,
        detail="Could not extract text from PDF. Please upload a text-based PDF."
        )


    jd_text = jd.strip()

    # RAG Pipeline
    try:
        # Split resume into chunks
        chunks = split_text(resume_text)

        # Create embeddings + vector store (in-memory)
        embeddings = get_embeddings()
        vector_db = build_vector_store(chunks, embeddings)

        # Retrieve most relevant chunks using JD
        retrieved_docs = vector_db.similarity_search(jd_text, k=4)
        context = "\n\n".join(doc.page_content for doc in retrieved_docs)

    except Exception as e:
        traceback.print_exc()
        raise HTTPException(status_code=500, detail=str(e))


    # Prompt (Grounded with retrieved context)
    prompt = f"""
You are an expert technical recruiter.

Use ONLY the CONTEXT below to analyze the resume against the job description.
Do NOT use outside knowledge.

CONTEXT (Resume excerpts):
\"\"\"{context}\"\"\" 

JOB DESCRIPTION:
\"\"\"{jd_text}\"\"\" 

Return ONLY valid JSON in EXACT format:

{{
  "match_percentage": number (0-100),
  "matched_skills": list of strings,
  "missing_skills": list of strings,
  "resume_improvements": list of strings,
  "final_recommendation": string
}}
"""

    # Invoke LLM
    try:
        llm = get_llm()
        response = llm.invoke([HumanMessage(content=prompt)])
    except Exception as e:
        raise HTTPException(status_code=500, detail=f"LLM invocation failed: {str(e)}")

    # Parse JSON output
    try:
        return extract_json(response.content)
    except Exception:
        return {
            "error": "LLM output parsing failed",
            "raw_output": response.content
        }
