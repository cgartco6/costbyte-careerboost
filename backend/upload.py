from fastapi import APIRouter, UploadFile
from resume_processor import process_resume

router = APIRouter(prefix="/upload")

@router.post("/resume")
async def upload_resume(user_id: int, resume: UploadFile, photo: UploadFile, qualifications: UploadFile):
    file_paths = await process_resume(user_id, resume, photo, qualifications)
    return {"status": "processing", "files": file_paths}
