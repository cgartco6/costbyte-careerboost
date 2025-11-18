from fastapi import APIRouter, UploadFile
from ai_agents.synthetic_intelligence_core import rewrite_resume
from ai_agents.ai_pdf_generator import generate_pdf

router = APIRouter(prefix="/resume")

@router.post("/process")
async def process_resume(file: UploadFile):
    text = await file.read()
    ai_resume = rewrite_resume(text.decode("utf-8"))
    pdf_path = generate_pdf(ai_resume)
    return {"status": "success", "pdf": pdf_path}
