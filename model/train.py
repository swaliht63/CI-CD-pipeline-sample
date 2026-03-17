from sklearn.datasets import load_iris
from sklearn.ensemble import RandomForestClassifier
import joblib
import os

def train():
    X, y = load_iris(return_X_y=True)
    model = RandomForestClassifier()
    model.fit(X, y)

    os.makedirs("app", exist_ok=True)
    joblib.dump(model, "app/model.joblib")

if __name__ == "__main__":
    train()
