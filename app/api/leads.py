from fastapi import APIRouter, HTTPException
from app.schemas.schemas import Lead
from app.services.lead_analyzer import qualify_lead as analyze_with_ai

router = APIRouter()

@router.post("/qualify-lead")
def qualify_lead(lead: Lead):
    try:
        result = analyze_with_ai(lead.model_dump())
        return result
    except Exception as e:
        raise HTTPException(
            status_code=500,
            detail=f"Erro ao qualificar lead: {str(e)}"
        )
