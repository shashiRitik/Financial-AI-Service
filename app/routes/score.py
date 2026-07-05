from datetime import datetime, UTC
import uuid

from fastapi import APIRouter

from app.models.common import ApiResponse
from app.models.score import ScoreRequest, ScoreResponse
from app.services.ai_service import analyze_score

router = APIRouter()


@router.post(
    "/analyze-score",
    response_model=ApiResponse[ScoreResponse],
)
def analyze(request: ScoreRequest):

    result = analyze_score(request)

    return ApiResponse(
        success=True,
        message="Financial analysis generated successfully.",
        timestamp=datetime.now(UTC).isoformat(),
        request_id=f"FIN-{uuid.uuid4().hex[:8].upper()}",
        data=result,
    )