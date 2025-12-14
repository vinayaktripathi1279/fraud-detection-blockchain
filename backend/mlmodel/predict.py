#!/usr/bin/env python3
# predict.py
# Usage:
#   python predict.py '{"Time":0,"V1":1,...}'
# or:
#   echo '{"Time":0,"V1":1,...}' | python predict.py

import sys
import json
import os

# lazy imports (so we can show helpful errors if not installed)
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
    Read JSON either from argv[1] (preferred when Java passes it as a single arg)
    or from stdin (useful for manual testing).
    """
    raw = None
    if len(sys.argv) > 1:
        # join argv[1:] just in case the caller split the JSON by mistake
        raw = " ".join(sys.argv[1:])
    else:
        raw = sys.stdin.read()

    raw = raw.strip()
    if not raw:
        print("NO INPUT PROVIDED")
        sys.exit(1)

    try:
        data = json.loads(raw)
        return data, raw
    except Exception as e:
        # show raw input to help debugging (what Java actually sent)
        print("RAW_INPUT:", raw)
        print("PYTHON ERROR:", e)
        sys.exit(1)


def main():
    # columns expected by the model (same order used during training)
    columns = [
        "Time","V1","V2","V3","V4","V5","V6","V7","V8","V9",
        "V10","V11","V12","V13","V14","V15","V16","V17","V18","V19",
        "V20","V21","V22","V23","V24","V25","V26","V27","V28","Amount"
    ]

    # ensure we are running from folder where the model files exist
    # (the Java ProcessBuilder sets the working directory; otherwise adjust paths)
    model, scaler = load_models("fraud_model.pkl", "scaler.pkl")

    data, raw_input = read_input()

    # if the caller passed a top-level list, try to use the first item
    if isinstance(data, list) and len(data) > 0:
        data = data[0]

    if not isinstance(data, dict):
        print("INPUT MUST BE A JSON OBJECT (or an array with one object).")
        sys.exit(1)

    # fill missing features with 0 (or you can choose another default)
    for col in columns:
        if col not in data:
            data[col] = 0

    # Build dataframe in the correct column order
    try:
        df = pd.DataFrame([data], columns=columns)
    except Exception as e:
        print("ERROR BUILDING DATAFRAME:", e)
        print("RAW_INPUT:", raw_input)
        sys.exit(1)

    # Scale and predict
    try:
        scaled = scaler.transform(df)
    except Exception as e:
        print("SCALER TRANSFORM ERROR:", e)
        sys.exit(1)

    try:
        pred = model.predict(scaled)[0]
    except Exception as e:
        print("MODEL PREDICTION ERROR:", e)
        sys.exit(1)

    result = {
        "fraud": bool(int(pred)),
        "message": "Fraud Transaction" if int(pred) == 1 else "Safe Transaction"
    }

    # Java expects plain JSON string; print to stdout
    print(json.dumps(result))


if __name__ == "__main__":
    main()
