import time

from google import genai
from google.genai import types

from tenacity import retry, stop_after_attempt, wait_fixed

from app.config import GEMINI_API_KEY, MODEL_NAME
from app.models.score import ScoreRequest, ScoreResponse
from app.services.prompt_service import build_score_prompt
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

        logger.info("Financial score analysis completed successfully")

        return response.parsed

    except Exception as e:
        logger.exception("Gemini API Error")

        raise RuntimeError(
            "Gemini Analysis Failed"
        ) from e