import joblib
import pandas as pd
from pathlib import Path

from sklearn.metrics import (
    classification_report,
    confusion_matrix,
)

# Load the held-out test data. This data is never used for fitting.
BACKEND_DIR = Path(__file__).resolve().parents[3]
df = pd.read_csv(BACKEND_DIR / "datasets" / "test" / "test.csv")

X = df["clean_text"]
y = df["label"]

# Load vectorizer
vectorizer = joblib.load(
    BACKEND_DIR / "app" / "ai" / "models" / "tfidf_vectorizer.pkl"
)

X = vectorizer.transform(X)

# Load model
model = joblib.load(
    BACKEND_DIR / "app" / "ai" / "models" / "scam_classifier.pkl"
)

predictions = model.predict(X)

print("=" * 60)
print("Classification Report")
print("=" * 60)

print(classification_report(y, predictions))

print("=" * 60)
print("Confusion Matrix")
print("=" * 60)

print(confusion_matrix(y, predictions))
