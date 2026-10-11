from sentence_transformers import SentenceTransformer
import joblib
import torch

LABELS = {0: "negative", 1: "neutral", 2: "positive"}


def _get_device():
    if torch.cuda.is_available():
        return "cuda"
    else:
        return "cpu"


def _load_scikitlearn_model(path: str):
    with open(path, "rb") as f:
        model = joblib.load(f)
    return model


def _load_sentence_transformer_model(path: str):
    model = SentenceTransformer(path)
    return model


class Inference:
    def __init__(self, sklearn_model_path: str, sentence_transformer_model_path: str):
        self.sklearn_model = joblib.load(sklearn_model_path)
        self.sentence_transformer_model = _load_sentence_transformer_model(
            sentence_transformer_model_path
        )
        self.device = _get_device()

    def predict(self, text: str):
        embedding = self.sentence_transformer_model.encode([text], device=self.device)
        prediction = self.sklearn_model.predict(embedding)
        predicted_label = LABELS[prediction[0]]
        return predicted_label
