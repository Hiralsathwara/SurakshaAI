import pandas as pd

# Load raw dataset
df = pd.read_csv("datasets/raw/1India_Cyber_Scam_Hinglish_Dataset.csv")

print("=" * 50)
print("ORIGINAL DATASET")
print("=" * 50)

print("Original Shape:", df.shape)

print("\nOriginal Label Distribution:")
print(df["label"].value_counts())

print("\nOriginal Category Distribution:")
print(df["scam_category"].value_counts())

# Select required columns
df = df[["text", "label", "scam_category"]]

# Rename
df.rename(columns={"scam_category": "category"}, inplace=True)

print("\nRows before removing duplicates:", len(df))

duplicates = df.duplicated().sum()
print("Duplicate rows:", duplicates)

# Remove duplicates
df.drop_duplicates(inplace=True)

print("Rows after removing duplicates:", len(df))

# Missing values
print("\nMissing Values:")
print(df.isnull().sum())

# Remove missing values
df.dropna(inplace=True)

print("Rows after removing missing values:", len(df))

# Empty text
empty_rows = (df["text"].str.strip() == "").sum()
print("Empty text rows:", empty_rows)

df = df[df["text"].str.strip() != ""]

print("\nFINAL SHAPE:", df.shape)

print("\nFinal Label Distribution:")
print(df["label"].value_counts())

print("\nFinal Category Distribution:")
print(df["category"].value_counts())

# Save
df.to_csv("datasets/processed/final_dataset.csv", index=False)

print("\nDataset saved successfully.")