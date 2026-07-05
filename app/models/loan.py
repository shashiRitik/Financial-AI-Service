from pydantic import BaseModel


class LoanRequest(BaseModel):
    financial_score: int
    monthly_income: float
    monthly_expense: float
    current_emi: float
    loan_amount: float
    loan_tenure: int
    interest_rate: float
    estimated_emi: float
    emi_ratio: float
    eligible: bool


class ImprovementPlan(BaseModel):
    duration: str
    expected_result: str
    priority: str


class LoanResponse(BaseModel):
    eligible: bool
    eligibility: str
    reason: str
    risk: str
    recommendation: str
    next_action: str

    missing_requirements: list[str]

    improvement_plan: ImprovementPlan