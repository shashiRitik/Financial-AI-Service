from fastapi import APIRouter

from app.models.recommendation import (
    RecommendationRequest,
    RecommendationResponse,
)

from app.services.ai_service import (
    describe_recommendation,
)

router = APIRouter()


@router.post(
    "/recommendation-description",
    response_model=RecommendationResponse,
)
def recommendation_description(
    request: RecommendationRequest,
):

    return describe_recommendation(request)