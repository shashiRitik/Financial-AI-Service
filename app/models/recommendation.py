from pydantic import BaseModel


class RecommendationRequest(BaseModel):
    title: str
    priority: str
    score_improvement: str
    timeline: str
    business_context: str


class RecommendationResponse(BaseModel):
    title: str
    description: str