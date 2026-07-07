from fastapi import FastAPI
from app.routes.chat import router as chat_router

from app.routes.loan import router as loan_router

from app.routes.recommendation import router as recommendation_router



app = FastAPI(
    title="Financial AI Service",
    version="1.0.0"
)

app.include_router(chat_router)


@app.get("/")
def health():
    return {
        "service": "Financial AI Service",
        "status": "UP",
        "version": "1.0.0"
    }

from app.routes.score import router as score_router

app.include_router(score_router)

app.include_router(loan_router)

app.include_router(recommendation_router)
