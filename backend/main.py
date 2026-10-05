from fastapi import FastAPI

from backend.database import Base, engine

from backend.models.attendance import Attendance
from backend.models.infrastructure import Infrastructure

from backend.routes.attendance import router as attendance_router
from backend.routes.infrastructure import router as infrastructure_router


app = FastAPI(title="AI Training Centre Monitoring API")


Base.metadata.create_all(bind=engine)


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
app.include_router(infrastructure_router)