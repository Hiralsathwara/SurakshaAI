import pandas as pd

indian = pd.read_csv(
    "datasets/processed/indian_clean.csv"
)

uci = pd.read_csv(
    "datasets/processed/uci_clean.csv"
)

# Merge
df = pd.concat(
    [indian, uci],
    ignore_index=True
)

# Remove exact duplicate rows
df.drop_duplicates(inplace=True)

# Shuffle
df = df.sample(
    frac=1,
    random_state=42
).reset_index(drop=True)

df.to_csv(
    "datasets/processed/final_dataset.csv",
    index=False
)

print("="*50)
print("Merged Dataset")
print("="*50)

print(df.shape)

print(df["label"].value_counts())

print(df["source"].value_counts())