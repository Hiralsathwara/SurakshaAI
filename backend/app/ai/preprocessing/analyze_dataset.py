import pandas as pd
import json
import os


print(os.getcwd())


def analyze_csv(path):

    print("=" * 60)
    print("CSV FILE:", os.path.basename(path))

    print("Current Directory:", os.getcwd())
    print("Reading:", path)
    print("Absolute Path:", os.path.abspath(path))

    # df = pd.read_csv(path)
    df = pd.read_csv(
    path,
    sep="\t",
    header=None,
    names=["label", "text"]
)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nColumn Types:")

    for col in df.columns:
        sample = df[col].iloc[0]
        print(f"{col}: {type(sample)}")

    print("\nDuplicate Rows:") 
    try:
        print(df.duplicated().sum())
    except TypeError:
        df_temp = df.copy()

        # Convert list columns to strings
        for col in df_temp.columns:
            if df_temp[col].apply(lambda x: isinstance(x, list)).any():
                df_temp[col] = df_temp[col].astype(str)

        print(df_temp.duplicated().sum())
        

    print("=" * 60)


def analyze_jsonl(path):

    print("=" * 60)
    print("JSONL FILE:", os.path.basename(path))

    records = []

    with open(path, "r", encoding="utf-8") as f:
        for line in f:
            records.append(json.loads(line))

    df = pd.DataFrame(records)

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nColumn Types:")
    for col in df.columns:
        print(f"{col}: {type(df[col].iloc[0])}")

    print("\nDuplicate Rows:")

    try:
        # Convert any list/dict columns into strings
        df_copy = df.copy()

        for col in df_copy.columns:
            df_copy[col] = df_copy[col].apply(
                lambda x: json.dumps(x, sort_keys=True)
                if isinstance(x, (list, dict))
                else x
            )

        print(df_copy.duplicated().sum())

    except Exception as e:
        print("Could not check duplicates.")
        print(e)

    print("=" * 60)

def analyze_sms_spam(path):

    print("=" * 60)
    print("SMS SPAM DATASET")

    df = pd.read_csv(
        path,
        sep="\t",
        header=None,
        names=["label", "text"]
    )

    print("\nShape:")
    print(df.shape)

    print("\nColumns:")
    print(df.columns.tolist())

    print("\nFirst 5 Rows:")
    print(df.head())

    print("\nMissing Values:")
    print(df.isnull().sum())

    print("\nDuplicate Rows:")
    print(df.duplicated().sum())

    print("=" * 60)

if __name__ == "__main__":

    analyze_csv(
    r"datasets/raw/1India_Cyber_Scam_Hinglish_Dataset.csv"
)

analyze_jsonl(
    r"datasets/raw/2train_0.jsonl"
)

analyze_jsonl(
    r"datasets/raw/3INDIA-SPECIFIC-FRAUD-V1.jsonl"
)
analyze_sms_spam(
    r"datasets/raw/SMSSpamCollection"
)