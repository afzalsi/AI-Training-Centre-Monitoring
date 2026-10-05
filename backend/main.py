from fastapi import FastAPI

from backend.database import Base, engine

from backend.models.attendance import Attendance
from backend.models.infrastructure import Infrastructure
from backend.models.trainer import TrainerMonitoring

from backend.routes.attendance import router as attendance_router
from backend.routes.infrastructure import router as infrastructure_router
from backend.routes.trainer import router as trainer_router
from backend.routes.dashboard import router as dashboard_router


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
app.include_router(trainer_router)
app.include_router(dashboard_router)