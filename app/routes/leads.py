from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app import schemas, crud
from app.database import SessionLocal

router = APIRouter(prefix="/leads", tags=["Leads"])

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/")
def create_lead(lead: schemas.LeadCreate, db: Session = Depends(get_db)):
    return crud.create_lead(db, lead)

@router.get("/")
def get_leads(db: Session = Depends(get_db)):
    return crud.get_all_leads(db)

@router.put("/{lead_id}")
def update_lead(lead_id: int, updates: schemas.LeadUpdate, db: Session = Depends(get_db)):
    return crud.update_lead(db, lead_id, updates)