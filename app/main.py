from fastapi import FastAPI
from app.database import Base, engine
from app.routes import leads, dashboard
from fastapi.middleware.cors import CORSMiddleware

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Gharpayy CRM")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

app.include_router(leads.router)
app.include_router(dashboard.router)

@app.get("/")
def root():
    return {"message": "CRM Running"}