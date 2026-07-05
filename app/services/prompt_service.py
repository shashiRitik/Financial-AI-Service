from app.models.score import ScoreRequest
from app.prompts.score_prompt import SCORE_PROMPT_TEMPLATE
from app.models.loan import LoanRequest
from app.prompts.loan_prompt import LOAN_PROMPT_TEMPLATE

def build_score_prompt(request: ScoreRequest):

    return SCORE_PROMPT_TEMPLATE.format(

        score=request.score,
        income=request.income,
        expense=request.expense,
        saving=request.saving,
        shopping=request.shopping,
        fuel=request.fuel,
        emi=request.emi,
    )




def build_loan_prompt(request: LoanRequest):

    return LOAN_PROMPT_TEMPLATE.format(

        financial_score=request.financial_score,

        monthly_income=request.monthly_income,

        monthly_expense=request.monthly_expense,

        current_emi=request.current_emi,

        loan_amount=request.loan_amount,

        loan_tenure=request.loan_tenure,

        interest_rate=request.interest_rate,

        estimated_emi=request.estimated_emi,

        emi_ratio=request.emi_ratio,

        eligible=request.eligible,
    )