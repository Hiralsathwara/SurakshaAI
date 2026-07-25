from app.knowledge.fraud_knowledge import FRAUD_KNOWLEDGE


class ExplanationService:

    def generate(self, prediction, message):

        if prediction == "Safe":
            return {
                "risk_level": "Low",
                "category": "Safe Message",
                "reason": [
                    "No scam indicators detected."
                ],
                "recommendation": [
                    "No action required."
                ]
            }

        message = message.lower()

        if "kyc" in message:
            category = "bank_kyc"

        elif "otp" in message:
            category = "otp"

        elif "upi" in message:
            category = "upi_refund"

        elif "lottery" in message:
            category = "lottery"

        else:
            category = "general_spam"

        return FRAUD_KNOWLEDGE.get(
            category,
            FRAUD_KNOWLEDGE["general_spam"]
        )


explanation_service = ExplanationService()