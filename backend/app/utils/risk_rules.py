def get_risk_level(
    prediction: str,
    confidence: float
):
    """
    Generate risk level based on prediction
    and confidence score.
    """

    # Safe messages are always Low risk
    if prediction == "Safe":
        return "Low"

    # Scam confidence rules
    if confidence >= 95:
        return "Critical"

    elif confidence >= 80:
        return "High"

    elif confidence >= 60:
        return "Medium"

    else:
        return "Low"