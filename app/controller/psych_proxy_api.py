from fastapi import APIRouter

from app.services.psych_proxy_service import run_psycho_twin

router = APIRouter()
@router.post("/psych-proxy")
def psych_proxy(user_id: str, session: dict):
    return run_psycho_twin(user_id, session)
