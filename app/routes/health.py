from datetime import datetime

from fastapi import APIRouter

from app.config import MODEL_NAME

router = APIRouter()

START_TIME = datetime.now()


@router.get("/health")
def health():

    uptime = datetime.now() - START_TIME

    return {
        "status": "UP",
        "version": "1.0.0",
        "model": MODEL_NAME,
        "environment": "development",
        "uptime": str(uptime).split(".")[0],
    }