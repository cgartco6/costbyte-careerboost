from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from backend.database import Base, engine
from backend.routers import auth, applicants, dashboard, uploads, payment_router

# Auto-generate tables
Base.metadata.create_all(bind=engine)

app = FastAPI(title="AI Job Platform", version="1.0")

# CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Routers
app.include_router(auth.router, prefix="/auth", tags=["Authentication"])
app.include_router(applicants.router, prefix="/applicants", tags=["Applicants"])
app.include_router(dashboard.router, prefix="/dashboard", tags=["Dashboard"])
app.include_router(uploads.router, prefix="/uploads", tags=["Uploads"])
app.include_router(payment_router.router, prefix="/payments", tags=["Payments"])

@app.get("/")
def home():
    return {"status": "running", "project": "AI Job Platform"}
