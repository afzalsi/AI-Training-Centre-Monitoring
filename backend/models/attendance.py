from sqlalchemy import Column, Integer, String, Float
from backend.database import Base


class Attendance(Base):
    __tablename__ = "attendance"

    id = Column(Integer, primary_key=True, index=True)
    centre_id = Column(String, index=True)
    total_students = Column(Integer)
    present_students = Column(Integer)
    attendance_percentage = Column(Float)