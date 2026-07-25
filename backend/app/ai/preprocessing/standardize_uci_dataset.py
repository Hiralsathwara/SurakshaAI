import pandas as pd

# Read tab-separated file
df = pd.read_csv(
    "datasets/raw/SMSSpamCollection",
    sep="\t",
    header=None,
    names=["label", "text"]
)

# Convert labels
df["label"] = df["label"].map({
    "ham": 0,
    "spam": 1
})

# Add category
df["category"] = df["label"].map({
    0: "none",
    1: "general_spam"
})

# Add language
df["language"] = "english"

# Add source
df["source"] = "uci"

# Arrange columns
df = df[
    [
        "text",
        "label",
        "category",
        "language",
        "source"
    ]
]

df.to_csv(
    "datasets/processed/uci_clean.csv",
    index=False
)

print(df.head())
print(df.shape)