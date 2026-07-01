from flask import Flask, request, jsonify
import pandas as pd
import joblib
from agent import explain_transaction

app = Flask(__name__)

# Load model
model = joblib.load("models/fraud_model.pkl")

# Load feature names
model_columns = joblib.load("models/model_columns.pkl")

@app.route("/")
def home():
    return "Fraud Detection API is Running!"

@app.route("/predict", methods=["POST"])
def predict():
    try:
        data = request.get_json()

        required_fields = [
            "step",
            "type",
            "amount",
            "oldbalanceOrg",
            "newbalanceOrig",
            "oldbalanceDest",
            "newbalanceDest",
            "isFlaggedFraud"
        ]

        for field in required_fields:
            if field not in data:
                return jsonify({"error": f"Missing field: {field}"}), 400

        transaction = pd.DataFrame([data])

        transaction = pd.get_dummies(transaction, columns=["type"])

        for column in model_columns:
            if column not in transaction.columns:
                transaction[column] = 0

        transaction = transaction[model_columns]

        prediction = model.predict(transaction)[0]
        probabilities = model.predict_proba(transaction)[0]
        confidence = max(probabilities) * 100

        result = "Fraud" if prediction == 1 else "Genuine"

        response = explain_transaction(
            data,
            result,
            confidence
        )

        return jsonify(response)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
