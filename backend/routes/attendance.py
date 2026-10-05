from fastapi import APIRouter, Depends
from pydantic import BaseModel
from sqlalchemy.orm import Session

from backend.database import get_db
from backend.models.attendance import Attendance

router = APIRouter(
    prefix="/api/attendance",
    tags=["Attendance"]
)


class AttendanceCreate(BaseModel):
    centre_id: str
    total_students: int
    present_students: int


@router.post("/")
def create_attendance(
    data: AttendanceCreate,
    db: Session = Depends(get_db)
):
    if data.total_students <= 0:
        return {"error": "total_students must be greater than 0"}

    if data.present_students < 0:
        return {"error": "present_students cannot be negative"}

    if data.present_students > data.total_students:
        return {
            "error": "present_students cannot exceed total_students"
        }

    attendance_percentage = (
        data.present_students / data.total_students
    ) * 100

    record = Attendance(
        centre_id=data.centre_id,
        total_students=data.total_students,
        present_students=data.present_students,
        attendance_percentage=attendance_percentage
    )

    db.add(record)
    db.commit()
    db.refresh(record)

    return {
        "id": record.id,
        "centre_id": record.centre_id,
        "total_students": record.total_students,
        "present_students": record.present_students,
        "attendance_percentage": round(
            record.attendance_percentage, 2
        )
    }


@router.get("/")
def get_attendance(db: Session = Depends(get_db)):
    records = db.query(Attendance).all()

    return records