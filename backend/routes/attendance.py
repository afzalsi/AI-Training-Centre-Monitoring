from fastapi import APIRouter

router = APIRouter(
    prefix="/api/attendance",
    tags=["Attendance"]
)


@router.get("/")
def get_attendance():
    return {
        "centre_id": "CENTRE001",
        "total_students": 30,
        "present_students": 27,
        "attendance_percentage": 90
    }