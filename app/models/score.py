from pydantic import BaseModel


class ScoreRequest(BaseModel):
    score: int
    income: float
    expense: float
    saving: float
    shopping: float
    fuel: float
    emi: float


class FinancialInsight(BaseModel):
    category: str
    impact: str
    reason: str
    priority: str


class TopPriority(BaseModel):
    title: str
    reason: str
    estimated_impact: str

class ScoreResponse(BaseModel):
    financial_score: int
    risk_level: str
    risk_color: str = ""
    confidence: int = 0

    summary: str
    strengths: list[str]
    weaknesses: list[str]
    recommendations: list[str]
    next_month_goal: str

    insights: list[FinancialInsight]
    top_priority: TopPriority