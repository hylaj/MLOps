import os
from fastapi import FastAPI
from api.models.sentiment import SentimentRequest, SentimentResponse


os.makedirs("api/models", exist_ok=True)

app = FastAPI()


@app.post("/predict")
def predict(request: SentimentRequest) -> SentimentResponse:
    return SentimentResponse(prediction="positive")
