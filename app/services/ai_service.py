from google import genai
from google.genai import types

from app.config import GEMINI_API_KEY, MODEL_NAME
from app.models.score import ScoreRequest, ScoreResponse
from app.services.prompt_service import build_score_prompt

client = genai.Client(api_key=GEMINI_API_KEY)


def ask_ai(message: str) -> str:
    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=message,
    )
    return response.text


def analyze_score(request: ScoreRequest) -> ScoreResponse:
    prompt = build_score_prompt(request)

    config = types.GenerateContentConfig(
        temperature=0.2,
        max_output_tokens=2048,
        response_mime_type="application/json",
        response_schema=ScoreResponse,
    )

    response = client.models.generate_content(
        model=MODEL_NAME,
        contents=prompt,
        config=config,
    )

    if response.parsed is None:
        raise ValueError("Gemini failed to generate structured response.")

    return response.parsed