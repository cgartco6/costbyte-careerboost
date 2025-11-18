from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.transaction import Transaction

router = APIRouter()

@router.post("/log")
def log_payment(user_id: int, amount: float, db: Session = Depends(get_db)):
    entry = Transaction(user_id=user_id, amount=amount)
    db.add(entry)
    db.commit()
    return {"message": "Logged"}
