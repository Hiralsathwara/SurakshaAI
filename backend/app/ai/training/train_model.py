import os
import joblib
import pandas as pd

from sklearn.linear_model import LogisticRegression
from pathlib import Path

# -----------------------------
# Load Dataset
# -----------------------------

BACKEND_DIR = Path(__file__).resolve().parents[3]
df = pd.read_csv(BACKEND_DIR / "datasets" / "train" / "train.csv")

X = df["clean_text"]
y = df["label"]

# -----------------------------
# Load TF-IDF Vectorizer
# -----------------------------

vectorizer = joblib.load(
    BACKEND_DIR / "app" / "ai" / "models" / "tfidf_vectorizer.pkl"
)

X = vectorizer.transform(X)

print("Training Samples :", X.shape[0])

# -----------------------------
# Train Model
# -----------------------------

model = LogisticRegression(
    max_iter=1000,
    random_state=42
)

model.fit(X, y)

# -----------------------------
# Save Model
# -----------------------------

models_dir = BACKEND_DIR / "app" / "ai" / "models"
os.makedirs(models_dir, exist_ok=True)

joblib.dump(
    model,
    models_dir / "scam_classifier.pkl"
)

print("\nModel Saved Successfully!")
