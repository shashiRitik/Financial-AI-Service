from fastapi import APIRouter

from app.models.score import ScoreRequest, ScoreResponse
from app.services.ai_service import analyze_score

router = APIRouter()


@router.post("/analyze-score", response_model=ScoreResponse)
def analyze(request: ScoreRequest):
    return analyze_score(request)