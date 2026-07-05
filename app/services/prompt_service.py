from app.models.score import ScoreRequest
from app.prompts.score_prompt import SCORE_PROMPT_TEMPLATE


def build_score_prompt(request: ScoreRequest) -> str:
    return SCORE_PROMPT_TEMPLATE.format(
        score=request.score,
        income=request.income,
        expense=request.expense,
        saving=request.saving,
        shopping=request.shopping,
        fuel=request.fuel,
        emi=request.emi,
    )