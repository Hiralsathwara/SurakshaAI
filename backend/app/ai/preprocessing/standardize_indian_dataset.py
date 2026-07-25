import pandas as pd

# Load
df = pd.read_csv("datasets/raw/1India_Cyber_Scam_Hinglish_Dataset.csv")

# Keep required columns
df = df[[
    "text",
    "label",
    "scam_category",
    "language_style"
]]

# Rename columns
df.rename(columns={
    "scam_category": "category",
    "language_style": "language"
}, inplace=True)

# Add source column
df["source"] = "indian"

# Save
df.to_csv(
    "datasets/processed/indian_clean.csv",
    index=False
)

print(df.head())
print(df.shape)