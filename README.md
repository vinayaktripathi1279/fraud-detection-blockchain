# Fraud Detection System using Machine Learning & Spring Boot

## 📌 Overview
This project is a **Fraud Detection System** that predicts whether a financial transaction is **fraudulent or safe** using a Machine Learning model.

The system is built using:
- **Machine Learning (Python)**
- **Spring Boot (Java backend)**
- **HTML, CSS, JavaScript (Frontend UI)**

The backend communicates with a Python ML model to generate predictions and returns the result to the UI or API clients.

---

## 🎯 Features
- Predicts **Fraud / Safe Transaction**
- Uses a trained ML model (Random Forest)
- REST API built with Spring Boot
- Frontend UI for manual testing
- API testing using Talend API Tester
- Handles real-world feature vectors (Time, V1–V28, Amount)

---

## 🛠 Tech Stack

### Backend
- Java
- Spring Boot
- Jackson (JSON handling)

### Machine Learning
- Python
- Pandas
- NumPy
- Scikit-learn
- Joblib / Pickle

### Frontend
- HTML
- CSS
- JavaScript (Fetch API)

### Tools
- Talend API Tester (Free Version)
- Git & GitHub

## 🧠 Machine Learning Model
- **Algorithm**: Random Forest Classifier
- **Dataset**: Credit Card Fraud Detection Dataset
- **Preprocessing**:
  - Feature scaling using StandardScaler
- **Model Output**:
  - Binary classification:
    - `1` → Fraud
    - `0` → Safe

The trained model and scaler are saved as:
- `fraud_model.pkl`
- `scaler.pkl`

## 🏗 Project Architecture

The project follows a simple client–server architecture where the frontend communicates with a Spring Boot backend, which in turn interacts with a Python-based Machine Learning model.



