import os
from dotenv import load_dotenv

load_dotenv()

class Settings:
    PROJECT_NAME = "AI Job Platform"
    SECRET_KEY = os.getenv("SECRET_KEY", "supersecretfallback")
    ALGORITHM = "HS256"
    ACCESS_TOKEN_EXPIRE_MINUTES = 120

    DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///./jobs.db")
    UPLOAD_DIR = "uploads/"
    RESUME_DIR = "uploads/resumes/"
    MAX_UPLOAD_MB = 25

settings = Settings()
