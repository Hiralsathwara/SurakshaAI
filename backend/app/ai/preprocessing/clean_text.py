import re
import html
import emoji
from bs4 import BeautifulSoup


def clean_text(text: str) -> str:
    """
    Clean scam message text while preserving Hinglish words.
    """

    # Handle None values
    if text is None:
        return ""

    # Convert to string
    text = str(text)

    # Convert HTML entities
    text = html.unescape(text)

    # Remove HTML tags
    text = BeautifulSoup(text, "html.parser").get_text()

    # Lowercase
    text = text.lower()

    # Remove URLs
    text = re.sub(r"http\S+|www\S+", " ", text)

    # Remove Email IDs
    text = re.sub(r"\S+@\S+", " ", text)

    # Remove Phone Numbers (7+ digits)
    text = re.sub(r"\b\d{7,}\b", " ", text)

    # Remove Emojis
    text = emoji.replace_emoji(text, replace="")

    # Keep only letters, numbers and spaces
    text = re.sub(r"[^a-zA-Z0-9\s]", " ", text)

    # Remove Extra Spaces
    text = re.sub(r"\s+", " ", text).strip()

    return text
if __name__ == "__main__":

    sample = """
    🚨 Dear Customer!!

    Your SBI account is blocked.

    Visit https://fakebank.com

    Call 9876543210 immediately.

    धन्यवाद 😊
    """

    print("Original:\n")
    print(sample)

    print("\nCleaned:\n")
    print(clean_text(sample))