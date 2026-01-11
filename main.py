from fastapi import FastAPI
from api.routes import router
from dotenv import load_dotenv

load_dotenv()

app = FastAPI(
    title="Resume–JD Analyzer (RAG + LLaMA)",
    description="Analyze resume vs job description using Retrieval-Augmented Generation",
    version="1.0"
)

app.include_router(router)

@app.get("/")
def health_check():
    return {"status": "API is running"}
