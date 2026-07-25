import pandas as pd
import matplotlib.pyplot as plt

# Load cleaned dataset
df = pd.read_csv("datasets/processed/final_dataset.csv")

print("="*50)
print("DATASET OVERVIEW")
print("="*50)

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())

print("\n")

# ------------------------------------
# Label Distribution
# ------------------------------------

print("="*50)
print("LABEL DISTRIBUTION")
print("="*50)

print(df["label"].value_counts())

df["label"].value_counts().plot(
    kind="bar",
    title="Scam vs Safe Messages"
)

plt.xlabel("Label")
plt.ylabel("Count")
plt.tight_layout()
plt.savefig("reports/figures/label_distribution1.png")
plt.close()

# ------------------------------------
# Scam Categories
# ------------------------------------

print("="*50)
print("TOP SCAM CATEGORIES")
print("="*50)

print(df["category"].value_counts())

df["category"].value_counts().head(10).plot(
    kind="bar",
    title="Top Scam Categories"
)

plt.xticks(rotation=45)

plt.tight_layout()
plt.savefig("reports/figures/label_distribution2.png")
plt.close()

# ------------------------------------
# Message Length
# ------------------------------------

df["message_length"] = df["text"].apply(len)

print("="*50)
print("MESSAGE LENGTH")
print("="*50)

print(df["message_length"].describe())

plt.hist(df["message_length"], bins=30)

plt.title("Message Length Distribution")

plt.xlabel("Characters")

plt.ylabel("Frequency")

plt.tight_layout()
plt.savefig("reports/figures/label_distribution3.png")
plt.close()

