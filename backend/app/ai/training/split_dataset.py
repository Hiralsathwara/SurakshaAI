"""Create deterministic train and test CSV files for the scam classifier."""

from pathlib import Path

import pandas as pd
from sklearn.model_selection import train_test_split


BACKEND_DIR = Path(__file__).resolve().parents[3]
SOURCE_DATASET = BACKEND_DIR / "datasets" / "processed" / "final_dataset_clean.csv"
TRAIN_DATASET = BACKEND_DIR / "datasets" / "train" / "train.csv"
TEST_DATASET = BACKEND_DIR / "datasets" / "test" / "test.csv"


def main():
    dataset = pd.read_csv(SOURCE_DATASET).dropna(subset=["clean_text", "label"])

    train_data, test_data = train_test_split(
        dataset,
        test_size=0.20,
        random_state=42,
        stratify=dataset["label"],
    )

    TRAIN_DATASET.parent.mkdir(parents=True, exist_ok=True)
    TEST_DATASET.parent.mkdir(parents=True, exist_ok=True)

    train_data.to_csv(TRAIN_DATASET, index=False)
    test_data.to_csv(TEST_DATASET, index=False)

    print(f"Training data: {len(train_data)} rows -> {TRAIN_DATASET}")
    print(f"Testing data:  {len(test_data)} rows -> {TEST_DATASET}")


if __name__ == "__main__":
    main()
