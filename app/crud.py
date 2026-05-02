from sqlalchemy.orm import Session
from app import models

def create_lead(db: Session, lead):
    db_lead = models.Lead(**lead.dict())
    db.add(db_lead)
    db.commit()
    db.refresh(db_lead)
    return db_lead

def get_all_leads(db: Session):
    return db.query(models.Lead).all()

def update_lead(db: Session, lead_id: int, updates):
    lead = db.query(models.Lead).filter(models.Lead.id == lead_id).first()
    if not lead:
        return None

    for key, value in updates.dict(exclude_unset=True).items():
        setattr(lead, key, value)

    db.commit()
    db.refresh(lead)
    return lead

def get_dashboard_stats(db: Session):
    total = db.query(models.Lead).count()
    closed = db.query(models.Lead).filter(models.Lead.status == "Closed").count()
    pending = db.query(models.Lead).filter(models.Lead.status != "Closed").count()

    return {
        "total_leads": total,
        "closed_leads": closed,
        "pending_leads": pending
    }