from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.attendance import Attendance
from backend.models.infrastructure import Infrastructure
from backend.models.trainer import TrainerMonitoring

router = APIRouter(
    prefix="/api/dashboard",
    tags=["Dashboard"]
)


@router.get("/{centre_id}")
def get_dashboard(
    centre_id: str,
    db: Session = Depends(get_db)
):
    attendance = (
        db.query(Attendance)
        .filter(Attendance.centre_id == centre_id)
        .order_by(Attendance.id.desc())
        .first()
    )

    infrastructure = (
        db.query(Infrastructure)
        .filter(Infrastructure.centre_id == centre_id)
        .order_by(Infrastructure.id.desc())
        .first()
    )

    trainer = (
        db.query(TrainerMonitoring)
        .filter(TrainerMonitoring.centre_id == centre_id)
        .order_by(TrainerMonitoring.id.desc())
        .first()
    )

    return {
        "centre_id": centre_id,

        "attendance": (
            {
                "total_students": attendance.total_students,
                "present_students": attendance.present_students,
                "attendance_percentage": attendance.attendance_percentage
            }
            if attendance else None
        ),

        "infrastructure": (
            {
                "computers_detected": infrastructure.computers_detected,
                "projector_detected": infrastructure.projector_detected,
                "whiteboard_detected": infrastructure.whiteboard_detected,
                "fire_extinguisher_detected": infrastructure.fire_extinguisher_detected,
                "compliance_score": infrastructure.compliance_score
            }
            if infrastructure else None
        ),

        "trainer": (
            {
                "trainer_present": trainer.trainer_present,
                "activity_detected": trainer.activity_detected,
                "monitoring_status": trainer.monitoring_status
            }
            if trainer else None
        )
    }