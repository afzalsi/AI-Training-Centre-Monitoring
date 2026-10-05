from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.infrastructure import Infrastructure

router = APIRouter(
    prefix="/api/infrastructure",
    tags=["Infrastructure"]
)


class InfrastructureCreate(BaseModel):
    centre_id: str
    computers_detected: int
    projector_detected: bool
    whiteboard_detected: bool
    fire_extinguisher_detected: bool


@router.post("/")
def create_infrastructure(
    data: InfrastructureCreate,
    db: Session = Depends(get_db)
):
    if data.computers_detected < 0:
        return {
            "error": "computers_detected cannot be negative"
        }

    # Simple compliance calculation
    score = 0

    if data.computers_detected > 0:
        score += 25

    if data.projector_detected:
        score += 25

    if data.whiteboard_detected:
        score += 25

    if data.fire_extinguisher_detected:
        score += 25

    record = Infrastructure(
        centre_id=data.centre_id,
        computers_detected=data.computers_detected,
        projector_detected=data.projector_detected,
        whiteboard_detected=data.whiteboard_detected,
        fire_extinguisher_detected=data.fire_extinguisher_detected,
        compliance_score=score
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "id": record.id,
        "centre_id": record.centre_id,
        "computers_detected": record.computers_detected,
        "projector_detected": record.projector_detected,
        "whiteboard_detected": record.whiteboard_detected,
        "fire_extinguisher_detected": record.fire_extinguisher_detected,
        "compliance_score": record.compliance_score
    }


@router.get("/")
def get_infrastructure(db: Session = Depends(get_db)):
    records = db.query(Infrastructure).all()

    return records