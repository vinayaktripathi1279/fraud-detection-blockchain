# 🛡️ Fraud Detection System using Machine Learning, Spring Boot & Blockchain

![Java](https://img.shields.io/badge/Java-17-orange.svg)
![Spring Boot](https://img.shields.io/badge/Spring%20Boot-3.x-brightgreen.svg)
![Python](https://img.shields.io/badge/Python-3.11-blue.svg)
![Docker](https://img.shields.io/badge/Docker-Ready-blue.svg)
![Vercel](https://img.shields.io/badge/Vercel-Frontend-black.svg)
![Render](https://img.shields.io/badge/Render-Backend-teal.svg)

---

## 🌐 Live Demo & Deployment Links

| Component | Platform | Status / Link |
| :--- | :--- | :--- |
| **Frontend Dashboard UI** | **Vercel** | 🔗 [Live Vercel Demo](https://fraud-detection-blockchain.vercel.app) *(Deploy step below)* |
| **Backend REST API + ML** | **Render** | 🔗 [Live Render API Endpoint](https://fraud-detection-blockchain.onrender.com) *(Deploy step below)* |
| **GitHub Repository** | **GitHub** | 🔗 [vinayaktripathi1279/fraud-detection-blockchain](https://github.com/vinayaktripathi1279/fraud-detection-blockchain) |

---

## 📌 Overview

This project is a **Financial Fraud Detection & Cryptographic Verification System** designed to predict whether credit card transactions are **Fraudulent or Safe** using a Machine Learning model, while immutably logging validated transactions to a **Cryptographic Blockchain Ledger**.

```
[ Frontend (Vercel) ] ── (HTTP POST /api/ml/predict) ──> [ Spring Boot API (Render) ]
                                                                 │
                                                      (Executes predict.py)
                                                                 │
                                                       [ Scikit-Learn Model ]
                                                                 │
                                                      (Appends to Ledger)
                                                                 │
                                                       [ SHA-256 Blockchain ]
```

---

## 🎯 Features

- **Machine Learning Fraud Classification**: Evaluates transaction feature vectors (`Time`, `V1`–`V28`, `Amount`) using a Random Forest Classifier.
- **Blockchain Audit Ledger**: Cryptographically appends verified records into an immutable SHA-256 block structure.
- **Spring Boot REST Backend**: Manages process isolation between Java server and Python ML inference runtime.
- **Responsive Web UI**: Built with modern CSS & JavaScript for interactive feature evaluation and instant risk assessment.
- **Cloud Deployment Ready**: Containerized with multi-stage Docker build for Render and configured for Vercel edge deployment.

---

## 🛠 Tech Stack

* **Backend**: Java 17, Spring Boot, Jackson JSON, SHA-256 Cryptography
* **Machine Learning**: Python 3.11, Scikit-Learn (Random Forest), Pandas, NumPy, Joblib
* **Frontend**: HTML5, CSS3 (Inter Typography), Modern JavaScript (Fetch API)
* **DevOps**: Docker, Vercel, Render, Git / GitHub

---

## 🚀 How to Deploy

### Option 1: Deploy Backend to Render (Docker)
1. Log in to [Render](https://render.com/).
2. Click **New +** -> **Web Service**.
3. Connect your GitHub Repository: `vinayaktripathi1279/fraud-detection-blockchain`.
4. Select **Docker** as the Runtime.
5. Render will automatically read the root [Dockerfile](file:///c:/Users/vinay/Downloads/PROJECT/fraud-detection-blockchain/Dockerfile) and deploy your Spring Boot + Python ML container!
6. Copy your service URL (e.g. `https://fraud-detection-blockchain.onrender.com`).

### Option 2: Deploy Frontend to Vercel
1. Log in to [Vercel](https://vercel.com/).
2. Click **Add New** -> **Project**.
3. Import `vinayaktripathi1279/fraud-detection-blockchain`.
4. Set **Root Directory** to `frontend`.
5. Click **Deploy**!
6. *(Optional)* Update `ENV_API_URL` in [frontend/predict.js](file:///c:/Users/vinay/Downloads/PROJECT/fraud-detection-blockchain/frontend/predict.js) with your deployed Render Backend URL.

---

## 🔌 REST API Endpoints

### 1. Predict Fraud Probability
* **Endpoint**: `POST /api/ml/predict`
* **Content-Type**: `application/json`
* **Sample Request Payload**:
```json
"{\"Time\":0,\"V1\":-1.3598,\"V2\":-0.0727,\"V3\":2.5363,\"Amount\":149.62}"
```
* **Sample Response**:
```json
{
  "fraud": false,
  "message": "Safe Transaction"
}
```

### 2. View Blockchain Chain
* **Endpoint**: `GET /api/blockchain/chain`
* **Response**: List of block records containing index, timestamp, transaction data, hash, and previous hash.

### 3. Add Block Record
* **Endpoint**: `POST /api/blockchain/add`
* **Body**: Raw transaction string / payload.

---

## 💻 Local Setup & Execution

1. **Clone Repository**:
   ```bash
   git clone https://github.com/vinayaktripathi1279/fraud-detection-blockchain.git
   cd fraud-detection-blockchain
   ```

2. **Install Python Dependencies**:
   ```bash
   pip install pandas numpy scikit-learn joblib
   ```

3. **Run Spring Boot Backend**:
   ```bash
   cd backend
   ./mvnw spring-boot:run
   ```

4. **Access Web App**:
   Open browser at `http://localhost:8080` or open [frontend/index.html](file:///c:/Users/vinay/Downloads/PROJECT/fraud-detection-blockchain/frontend/index.html).
