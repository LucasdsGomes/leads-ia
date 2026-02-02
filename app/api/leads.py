from fastapi import APIRouter
from app.schemas.schemas import Lead

router = APIRouter()

@router.post("/qualify-lead")
def qualify_lead(lead: Lead):
    if "ceo" in lead.cargo.lower():
        return {
            "score": "QUENTE",
            "motivo": "Cargo decisor"
        }

    return {
        "score": "MORNO",
        "motivo": "Necessita análise"
    }
