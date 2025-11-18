from fastapi import APIRouter

router = APIRouter(prefix="/payment")

@router.post("/initiate")
def initiate_payment(user_id: int):
    return {
        "methods": ["Direct EFT FNB", "PayFast", "PayShap"],
        "amount": 500,
        "status": "Awaiting payment"
    }
