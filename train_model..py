import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, classification_report

# Load dataset
data = pd.read_csv("dataset/AIML Dataset.csv")
data = data.sample(n=200000, random_state=42)
print("Dataset loaded successfully!")
print("Rows:", len(data))

# Drop account number columns
data = data.drop(["nameOrig", "nameDest"], axis=1)

# Convert transaction type into numbers
data = pd.get_dummies(data, columns=["type"])

# Features
X = data.drop(["isFraud"], axis=1)

# Target
y = data["isFraud"]

# Split the dataset
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.20,
    random_state=42
)

print("Training model...")

# Create Random Forest model
model = RandomForestClassifier(
    n_estimators=100,
    random_state=42,
    n_jobs=-1
)

# Train
model.fit(X_train, y_train)

print("Training complete!")

# Test
predictions = model.predict(X_test)

print("\nAccuracy:")
print(accuracy_score(y_test, predictions))

print("\nClassification Report:")
print(classification_report(y_test, predictions))

# Save model
joblib.dump(model, "models/fraud_model.pkl")

# Save feature names
joblib.dump(X.columns.tolist(), "models/model_columns.pkl")

print("\nModel saved successfully!")