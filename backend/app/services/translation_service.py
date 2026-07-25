"""
===========================================================
        Translation Service
===========================================================
Gujarati / Hindi / English text processing
===========================================================
"""


def detect_language(text):

    if any(
        "\u0A80" <= char <= "\u0AFF"
        for char in text
    ):
        return "gu"

    return "en"



def translate_text(text):

    # Future translation integration
    # Google Translate / AI model can be added later

    return text