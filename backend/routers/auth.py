from fastapi import APIRouter, HTTPException
from models.user import UserCreate, UserLogin
from database import users
from utils.security import hash_password, verify_password, create_jwt

router = APIRouter(prefix="/auth")

@router.post("/register")
async def register(user: UserCreate):
    if users.find_one({"email": user.email}):
        raise HTTPException(400, "Email already registered")

    hashed = hash_password(user.password)
    users.insert_one({"email": user.email, "password": hashed})

    return {"message": "Registration successful"}

@router.post("/login")
async def login(user: UserLogin):
    db_user = users.find_one({"email": user.username})
    if not db_user or not verify_password(user.password, db_user["password"]):
        raise HTTPException(400, "Invalid credentials")

    token = create_jwt(db_user["email"])
    return {"access_token": token, "token_type": "bearer"}
