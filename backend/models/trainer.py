from sqlalchemy import Column, Integer, String, Boolean
from backend.database import Base


class TrainerMonitoring(Base):
    __tablename__ = "trainer_monitoring"

    id = Column(Integer, primary_key=True, index=True)
    centre_id = Column(String, index=True)
    trainer_present = Column(Boolean)
    activity_detected = Column(Boolean)
    monitoring_status = Column(String)