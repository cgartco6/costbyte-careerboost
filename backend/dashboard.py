from fastapi import APIRouter
from database import db

router = APIRouter(prefix="/dashboard")

@router.get("/data")
def dashboard_data():
    return {
        "users": db.users.count(),
        "revenue": db.transactions.sum("amount"),
        "jobs": db.jobs.count(),
        "rev_labels": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "rev_data": db.analytics.get_revenue_7days(),
        "user_labels": ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"],
        "user_data": db.analytics.get_users_7days()
    }
