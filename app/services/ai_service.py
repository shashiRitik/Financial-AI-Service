import time

from google import genai
from google.genai import types

from tenacity import retry, stop_after_attempt, wait_fixed

from app.config import GEMINI_API_KEY, MODEL_NAME

from app.models.score import ScoreRequest, ScoreResponse
from app.models.loan import LoanRequest, LoanResponse

from app.services.prompt_service import (
    build_score_prompt,
    build_loan_prompt,
)

from app.utils.logger import logger

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(message: str) -> str:
    logger.info("Calling Gemini Chat API")

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=message,
    )

    logger.info("Chat response received")

    return response.text.strip()


# =====================================================
# Financial Score Analysis
# =====================================================

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
)
def analyze_score(request: ScoreRequest) -> ScoreResponse:

    prompt = build_score_prompt(request)

    config = types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=2048,
        response_mime_type="application/json",
        response_schema=ScoreResponse,
    )

    try:
        logger.info(f"Calling Gemini Score API | Model: {MODEL_NAME}")

        start = time.time()

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=config,
        )

        elapsed = time.time() - start

        logger.info(f"Gemini response received in {elapsed:.2f} seconds")

        if response.parsed is None:
            logger.error("Gemini failed to return structured response.")
            logger.error(response.text)

            raise ValueError(
                "Gemini failed to return structured response."
            )

        result = response.parsed

        # Backend controlled fields
        result.financial_score = request.score

        if result.financial_score >= 80:
            result.confidence = 95
            result.risk_color = "GREEN"

        elif result.financial_score >= 60:
            result.confidence = 85
            result.risk_color = "YELLOW"

        else:
            result.confidence = 75
            result.risk_color = "RED"

        logger.info("Financial score analysis completed successfully")

        return result

    except Exception as e:
        logger.exception("Gemini Score API Error")

        raise RuntimeError(
            "Gemini Score Analysis Failed"
        ) from e


# =====================================================
# Loan Advisor
# =====================================================

@retry(
    stop=stop_after_attempt(3),
    wait=wait_fixed(2),
)
def analyze_loan(request: LoanRequest) -> LoanResponse:

    prompt = build_loan_prompt(request)

    config = types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=1024,
        response_mime_type="application/json",
        response_schema=LoanResponse,
    )

    try:
        logger.info(f"Calling Gemini Loan API | Model: {MODEL_NAME}")

        start = time.time()

        response = client.models.generate_content(
            model=MODEL_NAME,
            contents=prompt,
            config=config,
        )

        elapsed = time.time() - start

        logger.info(f"Loan response received in {elapsed:.2f} seconds")

        if response.parsed is None:
            logger.error("Gemini failed to return structured loan response.")
            logger.error(response.text)

            raise ValueError(
                "Gemini failed to return structured loan response."
            )

        logger.info("Loan analysis completed successfully")

        return response.parsed

    except Exception as e:
        logger.exception("Gemini Loan API Error")

        raise RuntimeError(
            "Loan Analysis Failed"
        ) from e