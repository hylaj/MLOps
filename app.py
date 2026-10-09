import inference
import os
from fastapi import FastAPI
from api.models.iris import PredictRequest, PredictResponse

os.makedirs("api/models", exist_ok=True)

app = FastAPI()
model = inference.load_model(os.path.join("api/models", "iris_model.joblib"))


@app.get("/")
def welcome_root():
    return {"message": "Welcome to the ML API"}


@app.get("/health")
def health_check():
    return {"status": "ok"}


@app.post("/predict")
def predict(request: PredictRequest) -> PredictResponse:
    prediction = inference.predict(model, request.model_dump())
    return PredictResponse(prediction=prediction)
