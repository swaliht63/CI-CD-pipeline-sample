# 🚀 ML CI/CD Pipeline Project

An end-to-end Machine Learning CI/CD pipeline using FastAPI, Docker, and GitHub Actions.

---

## 📌 Features

- Train ML model (Iris dataset)
- Save & load trained model
- FastAPI prediction service
- Automated testing with PyTest
- Docker containerization
- CI/CD using GitHub Actions

---

## 🧠 Tech Stack

- Python
- FastAPI
- Scikit-learn
- Docker
- GitHub Actions
- PyTest

---

## ▶️ Run Locally

pip install -r requirements.txt
python model/train.py
uvicorn app.main:app --reload

---

## 🐳 Run with Docker

docker build -t ml-cicd-app .
docker run -p 8000:8000 ml-cicd-app
