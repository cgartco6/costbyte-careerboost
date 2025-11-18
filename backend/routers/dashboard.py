from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from backend.database import get_db
from backend.models.user import User
from backend.models.transaction import Transaction

router = APIRouter()

@router.get("/stats")
def stats(db: Session = Depends(get_db)):
    users = db.query(User).count()
    payments = db.query(Transaction).count()
    revenue = db.query(Transaction).with_entities(Transaction.amount).all()
    revenue_total = sum([x[0] for x in revenue])

    return {
        "users": users,
        "payments": payments,
        "revenue": revenue_total
    }
