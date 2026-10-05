from fastapi import FastAPI
from backend.routes.attendance import router as attendance_router

app = FastAPI(title="AI Training Centre Monitoring API")


@app.get("/")
def root():
    return {
        "message": "AI Training Centre Monitoring API is running"
    }


@app.get("/health")
def health():
    return {
        "status": "healthy"
    }


app.include_router(attendance_router)