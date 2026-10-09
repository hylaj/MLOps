import joblib
import numpy as np


def load_model(path: str):
    with open(path, "rb") as f:
        model = joblib.load(f)
    return model


def predict(model, input_data: dict[str, float]) -> str:
    x = list(input_data.values())
    x = np.array(x).reshape(1, -1)
    y = model.predict(x)

    return y[0]
