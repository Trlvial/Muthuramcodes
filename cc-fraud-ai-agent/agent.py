def explain_transaction(data, prediction,confidence):
    """
    Generate an explanation for the prediction.
    """

    reasons = []

    # High transaction amount
    if data["amount"] > 200000:
        reasons.append("High transaction amount.")

    # Transaction type
    if data["type"] in ["TRANSFER", "CASH_OUT"]:
        reasons.append("Transaction type is commonly associated with fraud.")

    # Empty sender account
    if data["oldbalanceOrg"] == 0:
        reasons.append("Sender account had no balance before the transaction.")

    # Flagged fraud
    if data["isFlaggedFraud"] == 1:
        reasons.append("Transaction was flagged by the banking system.")

    if prediction == "Fraud":
        recommendation = "Block the transaction and verify the customer."
    else:
        recommendation = "Approve the transaction."

    return {
        "prediction": prediction,
        "confidence":f"{confidence:.2f}%",
        "reasons": reasons,
        "recommendation": recommendation
    }
