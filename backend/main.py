from fastapi import FastAPI, UploadFile, File, Depends
from routers import auth, applicants, dashboard, uploads
from payment_router import payment_router
from security import military_grade_security
from self_healing import auto_patch_system
import uvicorn

app = FastAPI(title="CostByte - CareerBoost")

app.include_router(auth.router)
app.include_router(applicants.router)
app.include_router(dashboard.router)
app.include_router(uploads.router)
app.include_router(payment_router)

@app.on_event("startup")
async def startup_event():
    auto_patch_system()
    military_grade_security()

if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8080)
