from sqlalchemy import Column, Integer, String, Boolean, Float
from backend.database import Base


class Infrastructure(Base):
    __tablename__ = "infrastructure"

    id = Column(Integer, primary_key=True, index=True)
    centre_id = Column(String, index=True)
    computers_detected = Column(Integer)
    projector_detected = Column(Boolean)
    whiteboard_detected = Column(Boolean)
    fire_extinguisher_detected = Column(Boolean)
    compliance_score = Column(Float)