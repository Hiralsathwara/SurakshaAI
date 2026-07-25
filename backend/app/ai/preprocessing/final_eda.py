import pandas as pd
import matplotlib.pyplot as plt

# Load final dataset
df = pd.read_csv("datasets/processed/final_dataset.csv")

print("=" * 60)
print("FINAL DATASET OVERVIEW")
print("=" * 60)

print("Shape:", df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nMissing Values:")
print(df.isnull().sum())

print("\n")

# -----------------------------------
# Label Distribution
# -----------------------------------

print("=" * 60)
print("LABEL DISTRIBUTION")
print("=" * 60)

print(df["label"].value_counts())

plt.figure(figsize=(6,4))
df["label"].value_counts().plot(kind="bar")

plt.title("Scam vs Safe Messages")
plt.xlabel("Label")
plt.ylabel("Count")

plt.tight_layout()
# plt.show()

plt.savefig("reports/figures/label_distribution4.png")
plt.close()

# -----------------------------------
# Category Distribution
# -----------------------------------

print("=" * 60)
print("TOP CATEGORIES")
print("=" * 60)

print(df["category"].value_counts())

plt.figure(figsize=(10,5))

df["category"].value_counts().head(10).plot(kind="bar")

plt.title("Top Scam Categories")

plt.xticks(rotation=30)

plt.tight_layout()

plt.savefig("reports/figures/category_distribution5.png")
plt.close()

# -----------------------------------
# Source Distribution
# -----------------------------------

print("=" * 60)
print("SOURCE DISTRIBUTION")
print("=" * 60)

print(df["source"].value_counts())

plt.figure(figsize=(5,4))

df["source"].value_counts().plot(kind="pie", autopct="%1.1f%%")

plt.ylabel("")

plt.title("Dataset Sources")

plt.savefig("reports/figures/label_distribution6.png")
plt.close()

# -----------------------------------
# Message Length
# -----------------------------------

df["message_length"] = df["text"].astype(str).apply(len)

print("=" * 60)
print("MESSAGE LENGTH")
print("=" * 60)

print(df["message_length"].describe())

plt.figure(figsize=(7,4))

plt.hist(df["message_length"], bins=30)

plt.title("Message Length Distribution")

plt.xlabel("Characters")

plt.ylabel("Frequency")

plt.tight_layout()

plt.savefig("reports/figures/label_distribution7.png")
plt.close()