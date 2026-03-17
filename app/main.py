from fastapi import FastAPI
from app.model import load_model
from app.predict import predict

app = FastAPI()
model = load_model()

@app.get("/")
def home():
    return {"message": "ML CI/CD Pipeline Running"}

@app.post("/predict")
def make_prediction(features: list):
    result = predict(model, features)
    return {"prediction": result}
