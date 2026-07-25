import os
import joblib
import pandas as pd
from pathlib import Path

from sklearn.feature_extraction.text import TfidfVectorizer

# Fit only on the training set so the test data remains unseen.
BACKEND_DIR = Path(__file__).resolve().parents[3]
df = pd.read_csv(BACKEND_DIR / "datasets" / "train" / "train.csv")

# Input text
X = df["clean_text"]

# Create TF-IDF Vectorizer
vectorizer = TfidfVectorizer(
    max_features=5000,
    ngram_range=(1, 2),      # Unigrams + Bigrams
    min_df=2,
    max_df=0.95
)

# Transform text into numerical features
X_vectorized = vectorizer.fit_transform(X)

print("=" * 60)
print("TF-IDF Vectorization Complete")
print("=" * 60)

print("Vocabulary Size:", len(vectorizer.vocabulary_))
print("Feature Matrix Shape:", X_vectorized.shape)

# Create models directory if it doesn't exist
models_dir = BACKEND_DIR / "app" / "ai" / "models"
os.makedirs(models_dir, exist_ok=True)

# Save vectorizer
joblib.dump(
    vectorizer,
    models_dir / "tfidf_vectorizer.pkl"
)

print("\nVectorizer saved successfully!")
