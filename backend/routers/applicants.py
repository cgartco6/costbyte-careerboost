from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.resume import Resume
from backend.models.user import User

router = APIRouter()

@router.get("/")
def list_applicants(db: Session = Depends(get_db)):
    return db.query(User).all()

@router.get("/{user_id}")
def applicant(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")

    resume = db.query(Resume).filter(Resume.user_id == user_id).first()
    return {"user": user, "resume": resume}

@router.delete("/{user_id}")
def delete_applicant(user_id: int, db: Session = Depends(get_db)):
    user = db.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(404, "User not found")

    db.delete(user)
    db.commit()
    return {"message": "User deleted"}
