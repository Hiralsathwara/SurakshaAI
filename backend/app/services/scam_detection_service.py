import joblib

from app.ai.preprocessing.clean_text import clean_text
from app.utils.risk_rules import get_risk_level
from app.utils.category_rules import detect_category
from app.utils.explanation_rules import generate_explanation
from app.utils.explanation_rules import generate_reasons
from app.utils.explanation_rules import generate_recommendations



class ScamDetectionService:

    def __init__(self):
        # Attempt to load pre-trained model artifacts. If they're missing,
        # fall back to a lightweight rule-based mode to avoid crashing the app.
        try:
            self.vectorizer = joblib.load(
                "app/ai/models/tfidf_vectorizer.pkl"
            )

            self.model = joblib.load(
                "app/ai/models/scam_classifier.pkl"
            )
            self.loaded = True
        except Exception:
            self.vectorizer = None
            self.model = None
            self.loaded = False

    def predict(self, message: str):

        cleaned = clean_text(message)
        # If model artifacts are not available, use a simple rule-based
        # heuristic to avoid blocking the API. Otherwise use the ML model.
        if not self.loaded:
            # Simple fallback: treat messages containing common scam keywords as Scam
            keywords = ["otp", "password", "pin", "upi", "bank", "click", "link"]
            lower = message.lower()
            is_scam = any(k in lower for k in keywords)
            prediction = 1 if is_scam else 0
            confidence = 85.0 if is_scam else 40.0
        else:
            vector = self.vectorizer.transform([cleaned])

            prediction = self.model.predict(vector)[0]

            probability = self.model.predict_proba(vector)[0]

            confidence = max(probability)
            confidence = round(
                max(probability) * 100,
                2
            )

        prediction_text = (
            "Scam"
            if prediction == 1
            else "Safe"
        )

        risk_level = get_risk_level(
            prediction_text,
            confidence
        )
        category = detect_category(message)

        explanation = generate_explanation(
        prediction_text,
        category
        )

        reasons = generate_reasons(message)
        recommendations = generate_recommendations(
            prediction_text,
            category
        )

        
        

        return {

            "message": message,

            "clean_text": cleaned,

            "prediction": prediction_text,

            "confidence": confidence,

            "risk_level": risk_level,

            "category": category,

            "explanation": explanation,

            "reasons": reasons,
        
            "recommendations": recommendations

}
        


# Create singleton instance
# The model loads once when FastAPI starts.
scam_service = ScamDetectionService()