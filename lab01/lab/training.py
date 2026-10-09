import os
import joblib
from sklearn.datasets import load_iris
from sklearn.linear_model import LogisticRegression


def load_data():
    iris = load_iris()
    return iris


def train_model(X, y):
    model = LogisticRegression(max_iter=200)
    model.fit(X, y)
    return model


def save_model(model, path: str):
    with open(path, "wb") as file:
        joblib.dump(model, file)


if __name__ == "__main__":
    iris = load_data()

    model = train_model(iris.data, iris.target_names[iris.target])
    save_model(model, path=os.path.join("api/models", "iris_model.joblib"))
    print("Model trained and saved")
