import os
from fastapi import FastAPI
from api.models.sentiment import PredictRequest, PredictResponse
from inference import Inference

app = FastAPI()
model = Inference(
    sklearn_model_path=os.path.join("model", "classifier.joblib"),
    sentence_transformer_model_path=os.path.join("model", "sentence_transformer.model"),
)


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    return PredictResponse(prediction=model.predict(request.text))
