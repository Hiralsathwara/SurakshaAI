def generate_explanation(
    prediction: str,
    category: str
):
    """
    Generate a human-friendly explanation
    based on prediction and category.
    """

    if prediction == "Safe":
        return (
            "This message does not show common scam "
            "patterns and appears to be safe."
        )

    explanations = {

        "Bank KYC Scam":
            "This message impersonates a bank and creates urgency to trick users into revealing banking credentials or completing fake KYC verification.",

        "Police Digital Arrest":
            "This message falsely claims legal action or arrest to create fear and pressure victims into sending money or sharing personal information.",

        "Lottery Scam":
            "This message promises fake prizes or lottery winnings to trick users into paying fees or sharing sensitive information.",

        "Amazon Scam":
            "This message pretends to be from an online shopping platform and attempts to steal payment or account information.",

        "Aadhaar Scam":
            "This message misuses Aadhaar verification or update requests to steal identity information.",

        "Relative Emergency Scam":
            "This message creates panic by pretending a family member or friend needs urgent financial help.",

        "General Scam":
            "This message contains suspicious patterns that are commonly used in phishing and online fraud.",

        "Unknown":
            "This message was classified as suspicious based on the machine learning model, but no specific scam category could be identified."

    }

    return explanations.get(
        category,
        "This message appears suspicious based on the AI analysis."
    )

def generate_reasons(message: str):
    """
    Generate reasons that explain
    why a message looks suspicious.
    """

    text = message.lower()

    reasons = []

    # Banking Keywords
    banking_keywords = [
        "bank",
        "kyc",
        "account",
        "otp",
        "atm",
        "debit",
        "credit",
        "sbi",
        "hdfc",
        "icici",
        "axis"
    ]

    if any(word in text for word in banking_keywords):
        reasons.append(
            "Contains banking keywords"
        )

    # Urgency Words
    urgency_keywords = [
        "urgent",
        "immediately",
        "now",
        "expire",
        "blocked",
        "suspend",
        "verify"
    ]

    if any(word in text for word in urgency_keywords):
        reasons.append(
            "Requests immediate action"
        )

    # Suspicious URL
    if (
        "http://" in text
        or
        "https://" in text
        or
        "www." in text
    ):
        reasons.append(
            "Contains suspicious link"
        )

    # Money
    money_keywords = [
        "prize",
        "reward",
        "lottery",
        "cash",
        "money",
        "win"
    ]

    if any(word in text for word in money_keywords):
        reasons.append(
            "Promises money or rewards"
        )

    # Personal Information
    personal_keywords = [
        "aadhaar",
        "aadhar",
        "pan",
        "password",
        "cvv",
        "pin"
    ]

    if any(word in text for word in personal_keywords):
        reasons.append(
            "Requests sensitive personal information"
        )

    # Safe Message
    if len(reasons) == 0:
        reasons.append(
            "No suspicious patterns detected"
        )

    return reasons

def generate_recommendations(
    prediction: str,
    category: str
):
    """
    Generate safety recommendations
    based on prediction and category.
    """

    if prediction == "Safe":

        return [

            "No immediate action is required.",

            "Always remain cautious when receiving messages from unknown senders.",

            "Verify unexpected requests before responding."

        ]

    recommendations = {

        "Bank KYC Scam": [

            "Never share your OTP, PIN, CVV, or banking credentials.",

            "Use only the official banking website or mobile app for verification.",

            "Contact your bank directly if you receive suspicious messages.",

            "Report cyber fraud by calling 1930."

        ],

        "Police Digital Arrest": [

            "Do not panic or transfer money immediately.",

            "No police department demands payment over phone or message.",

            "Contact your nearest police station to verify the claim.",

            "Report cyber fraud by calling 1930."

        ],

        "Lottery Scam": [

            "Ignore unexpected prize or lottery claims.",

            "Never pay processing or registration fees.",

            "Do not share personal or banking information.",

            "Report suspicious messages to 1930."

        ],

        "Amazon Scam": [

            "Verify your order only through the official Amazon app or website.",

            "Avoid clicking unknown delivery links.",

            "Do not share payment details with unknown callers.",

            "Report suspicious activity."

        ],

        "Aadhaar Scam": [

            "Verify Aadhaar updates only through the official UIDAI website.",

            "Never share OTPs related to Aadhaar verification.",

            "Ignore unofficial verification requests."

        ],

        "Relative Emergency Scam": [

            "Call your family member directly before sending money.",

            "Verify the emergency through another trusted contact.",

            "Never transfer money based only on a message."

        ],

        "General Scam": [

            "Avoid clicking suspicious links.",

            "Never share OTPs or passwords.",

            "Verify the sender before taking action.",

            "Report cyber fraud by calling 1930."

        ],

        "Unknown": [

            "Be cautious before responding.",

            "Verify the sender using official channels.",

            "Do not share sensitive personal information."

        ]

    }

    return recommendations.get(
        category,
        recommendations["Unknown"]
    )