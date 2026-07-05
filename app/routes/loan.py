from fastapi import APIRouter

from app.models.loan import LoanRequest, LoanResponse
from app.services.ai_service import analyze_loan

router = APIRouter()


@router.post(
    "/loan-advisor",
    response_model=LoanResponse,
)
def loan_advisor(request: LoanRequest):

    return analyze_loan(request)