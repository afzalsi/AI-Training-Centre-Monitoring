from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.trainer import TrainerMonitoring

router = APIRouter(
    prefix="/api/trainer",
    tags=["Trainer Monitoring"]
)


class TrainerMonitoringCreate(BaseModel):
    centre_id: str
    trainer_present: bool
    activity_detected: bool


@router.post("/")
def create_trainer_monitoring(
    data: TrainerMonitoringCreate,
    db: Session = Depends(get_db)
):
    if not data.centre_id.strip():
        return {
            "error": "centre_id cannot be empty"
        }

    if data.trainer_present and data.activity_detected:
        monitoring_status = "Active"
    elif data.trainer_present:
        monitoring_status = "Trainer Present - No Activity"
    elif data.activity_detected:
        monitoring_status = "Activity Detected - Trainer Not Present"
    else:
        monitoring_status = "Trainer Not Present"

    record = TrainerMonitoring(
        centre_id=data.centre_id,
        trainer_present=data.trainer_present,
        activity_detected=data.activity_detected,
        monitoring_status=monitoring_status
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "id": record.id,
        "centre_id": record.centre_id,
        "trainer_present": record.trainer_present,
        "activity_detected": record.activity_detected,
        "monitoring_status": record.monitoring_status
    }


@router.get("/")
def get_trainer_monitoring(
    db: Session = Depends(get_db)
):
    records = db.query(TrainerMonitoring).all()

    return records