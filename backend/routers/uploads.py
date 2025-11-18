import os
from fastapi import APIRouter, Depends, UploadFile, File, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.config import settings
from backend.models.resume import Resume

router = APIRouter()

@router.post("/resume/{user_id}")
def upload_resume(user_id: int, file: UploadFile = File(...), db: Session = Depends(get_db)):
    ext = file.filename.split(".")[-1].lower()
    if ext not in ["pdf", "docx"]:
        raise HTTPException(400, "Invalid file format")

    save_path = os.path.join(settings.RESUME_DIR, f"user_{user_id}.{ext}")

    with open(save_path, "wb") as f:
        f.write(file.file.read())

    record = Resume(user_id=user_id, file_path=save_path)
    db.add(record)
    db.commit()

    return {"message": "Uploaded successfully", "path": save_path}
