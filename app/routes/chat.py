from fastapi import APIRouter

from app.models.score_request import ChatRequest
from app.models.score_response import ChatResponse
from app.services.ai_service import ask_ai

router = APIRouter()


@router.post("/chat", response_model=ChatResponse)
def chat(request: ChatRequest):
    reply = ask_ai(request.message)
    return ChatResponse(reply=reply)