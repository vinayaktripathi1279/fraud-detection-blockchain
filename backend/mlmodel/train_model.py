import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import StandardScaler
from sklearn.ensemble import RandomForestClassifier
import joblib

# 1. Load dataset
df = pd.read_csv("fraud.csv")

# If dataset contains a column named 'Class' (0 = normal, 1 = fraud)
X = df.drop("Class", axis=1)
y = df["Class"]

# 2. Normalize features
scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)

# 3. Train-test split
X_train, X_test, y_train, y_test = train_test_split(X_scaled, y, test_size=0.2, random_state=42)

# 4. Train ML model
model = RandomForestClassifier()
model.fit(X_train, y_train)

# 5. Save model & scaler
joblib.dump(model, "fraud_model.pkl")
joblib.dump(scaler, "scaler.pkl")

print("Model trained successfully and saved!")
