from fastapi import FastAPI
from backend.routes import router
from backend.routers.resume import router as resume_router
from backend.routers.batch import router as batch_router




app = FastAPI(
    title="ATS Resume Analyzer API",
    description="Backend API for Resume Parsing and ATS Scoring",
    version="1.0.0"
)

app.include_router(router)
app.include_router(resume_router)
app.include_router(batch_router)



@app.get("/")
def home():
    return {
        "message": "Welcome to ATS Resume Analyzer API"
    }


@app.get("/health")
def health():
    return {
        "status": "running"
    }