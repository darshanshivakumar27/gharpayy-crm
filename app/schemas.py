from pydantic import BaseModel
from typing import Optional
from datetime import datetime

class LeadCreate(BaseModel):
    name: str
    phone: str
    location: str

class LeadUpdate(BaseModel):
    status: Optional[str] = None
    assigned_to: Optional[str] = None
    visit_time: Optional[datetime] = None

class LeadResponse(BaseModel):
    id: int
    name: str
    phone: str
    location: str
    status: str
    assigned_to: str
    visit_time: Optional[datetime]

    class Config:
        orm_mode = True