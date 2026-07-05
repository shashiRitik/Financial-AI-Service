from pydantic import BaseModel


class ScoreRequest(BaseModel):
    score: int
    income: float
    expense: float
    saving: float
    shopping: float
    fuel: float
    emi: float


class ScoreResponse(BaseModel):
    financial_score: int
    risk_level: str
    summary: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]
    next_month_goal: str