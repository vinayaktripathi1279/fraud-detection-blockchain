#!/usr/bin/env python3
# predict.py
# Usage:
#   python predict.py '{"Time":0,"V1":1,...}'
# or:
#   echo '{"Time":0,"V1":1,...}' | python predict.py

import sys
import json
import os

# Lazy imports
try:
    import pandas as pd
    import joblib
except Exception as e:
    print("PYTHON IMPORT ERROR:", str(e))
    sys.exit(1)


def load_models(model_path="fraud_model.pkl", scaler_path="scaler.pkl"):
    if not os.path.exists(model_path):
        print(f"MODEL FILE MISSING: {model_path}")
        sys.exit(1)
    if not os.path.exists(scaler_path):
        print(f"SCALER FILE MISSING: {scaler_path}")
        sys.exit(1)

    model = joblib.load(model_path)
    scaler = joblib.load(scaler_path)
    return model, scaler


def read_input():
    """
    Read JSON either from argv[1] (when Java passes it)
    or from stdin (manual testing).
    """
    if len(sys.argv) > 1:
        raw = " ".join(sys.argv[1:])
    else:
        raw = sys.stdin.read()

    raw = raw.strip()
    if not raw:
        print("NO INPUT PROVIDED")
        sys.exit(1)

    try:
        data = json.loads(raw)
        return data
    except Exception as e:
        print("RAW_INPUT:", raw)
        print("PYTHON ERROR:", e)
        sys.exit(1)


def main():
    # Model feature order
    columns = [
        "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
        "V10","V11","V12","V13","V14","V15","V16","V17","V18","V19",
        "V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
    ]

    # Load ML model and scaler
    model, scaler = load_models("fraud_model.pkl", "scaler.pkl")

    # Read input JSON
    data = read_input()

    # Handle array input
    if isinstance(data, list) and len(data) > 0:
        data = data[0]

    if not isinstance(data, dict):
        print("INPUT MUST BE A JSON OBJECT")
        sys.exit(1)

    # Fill missing values with 0
    for col in columns:
        if col not in data:
            data[col] = 0

    # Build dataframe
    df = pd.DataFrame([data], columns=columns)

    # Scale input
    scaled = scaler.transform(df)

    # ML prediction
    pred = model.predict(scaled)[0]

    # --------------------------------------------------
    # 🔴 DEMO OVERRIDE (FOR UI / PRESENTATION PURPOSE)
    # If Amount is very high, force fraud
    # --------------------------------------------------
    if float(data.get("Amount", 0)) > 50000:
        pred = 1

    # Prepare result
    result = {
        "fraud": bool(int(pred)),
        "message": "Fraud Transaction" if int(pred) == 1 else "Safe Transaction"
    }

    # Send JSON back to Spring Boot
    print(json.dumps(result))


if __name__ == "__main__":
    main()
