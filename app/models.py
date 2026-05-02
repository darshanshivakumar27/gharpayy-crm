from sqlalchemy import Column, Integer, String, DateTime
from datetime import datetime
from app.database import Base

class Lead(Base):
    __tablename__ = "leads"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    phone = Column(String)
    location = Column(String)
    status = Column(String, default="New")
    assigned_to = Column(String, default="Unassigned")
    visit_time = Column(DateTime, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)