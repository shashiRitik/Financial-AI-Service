from fastapi import FastAPI

app = FastAPI()
@app.get("/")

def health():
    return {
        "service": "Financial AI Service",
        "status": "UP",
        "version": "1.0.0",
        "environment": "development"
    }