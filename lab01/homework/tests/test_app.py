from fastapi.testclient import TestClient
from app import app, model

client = TestClient(app)


# inference should work for a few sample strings
def test_inference_on_sample_texts():
    for text in ["I love it", "This is terrible", "The meeting is at 5 pm"]:
        assert model.predict(text) in {"negative", "neutral", "positive"}


# output should be a valid JSON response


def test_predict_returns_valid_json():
    response = client.post("/predict", json={"text": "What a great lecture"})
    assert response.status_code == 200
    assert response.json()["prediction"] in {"negative", "neutral", "positive"}


# for an invalid input, validation should return a valid JSON with error explanation
def test_empty_text_returns_error_json():
    response = client.post("/predict", json={"text": ""})
    assert response.status_code == 422
    assert "detail" in response.json()


def test_missing_text_returns_error_json():
    response = client.post("/predict", json={})
    assert response.status_code == 422
    assert "detail" in response.json()
