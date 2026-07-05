from fastapi import APIRouter

from datetime import datetime, UTC
import uuid

from app.models.common import ApiResponse

from app.models.loan import LoanRequest, LoanResponse
from app.services.ai_service import analyze_loan

router = APIRouter()


@router.post(
    "/loan-advisor",
    response_model=ApiResponse[LoanResponse],
)
def loan_advisor(request: LoanRequest):

    result = analyze_loan(request)

    return ApiResponse(
        success=True,
        message="Loan analysis generated successfully.",
        timestamp=datetime.now(UTC).isoformat(),
        request_id=f"LOAN-{uuid.uuid4().hex[:8].upper()}",
        data=result,
    )