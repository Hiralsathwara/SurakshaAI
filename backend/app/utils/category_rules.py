def detect_category(message: str):
    """
    Detect scam category using keywords.
    """

    text = message.lower()

    categories = {

        "Bank KYC Scam": [
            "bank",
            "kyc",
            "account",
            "debit",
            "credit",
            "atm",
            "netbanking",
            "sbi",
            "hdfc",
            "icici",
            "axis"
        ],

        "Police Digital Arrest": [
            "police",
            "court",
            "arrest",
            "crime",
            "cyber",
            "fir",
            "cbi",
            "customs"
        ],

        "Lottery Scam": [
            "lottery",
            "winner",
            "prize",
            "reward",
            "lucky draw",
            "won"
        ],

        "Amazon Scam": [
            "amazon",
            "delivery",
            "parcel",
            "shipment",
            "refund"
        ],

        "Aadhaar Scam": [
            "aadhaar",
            "aadhar",
            "uidai"
        ],

        "Relative Emergency Scam": [
            "relative",
            "friend",
            "hospital",
            "urgent money",
            "accident"
        ],

        "General Scam": [
            "otp",
            "verify",
            "click",
            "link",
            "update",
            "urgent"
        ]

    }

    for category, keywords in categories.items():

        for keyword in keywords:

            if keyword in text:
                return category

    return "Unknown"