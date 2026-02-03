from fastapi import FastAPI
from app.api.leads import router as leads_router

app = FastAPI(title="AI Lead Qualifier")

app.include_router(leads_router, prefix="/leads")

@app.get("/health")
def health():
    return {"status": "ok"}