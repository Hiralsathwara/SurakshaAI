import pandas as pd

# from app.ai.preprocessing.clean_text import clean_text
from clean_text import clean_text


# Load dataset
df = pd.read_csv("datasets/processed/final_dataset.csv")

print("=" * 60)
print("Original Dataset:", df.shape)

# Apply cleaning
df["clean_text"] = df["text"].apply(clean_text)

# Remove empty rows after cleaning
df = df[df["clean_text"].str.strip() != ""]

print("Processed Dataset:", df.shape)

# Save
df.to_csv(
    "datasets/processed/final_dataset_clean.csv",
    index=False
)

print("\nDataset preprocessing completed successfully!")