import pytesseract
from PIL import Image


# Windows Tesseract Path


pytesseract.pytesseract.tesseract_cmd = (
    r"C:\Program Files\Tesseract-OCR\tesseract.exe"
)


def extract_text(image_path:str):

    image = Image.open(image_path)

    text = pytesseract.image_to_string(
        image
    )

    return text



def detect_scam(text:str):

    keywords = [

    # Urgency / Threat
    "urgent",
    "immediately",
    "act now",
    "hurry",
    "last chance",
    "limited time",
    "within 24 hours",
    "suspended",
    "blocked",
    "deactivated",
    "expired",

    # Verification / KYC Fraud
    "verify",
    "verification",
    "kyc",
    "update kyc",
    "complete kyc",
    "re verify",
    "account verification",
    "identity proof",
    "pan update",
    "aadhaar update",

    # Banking / UPI Fraud
    "upi",
    "upi id",
    "payment",
    "bank account",
    "bank details",
    "account number",
    "ifsc",
    "transaction",
    "failed transaction",
    "refund",
    "money transfer",
    "send money",
    "receive money",

    # OTP / Credential Theft
    "otp",
    "one time password",
    "pin",
    "cvv",
    "password",
    "login",
    "username",
    "credentials",

    # Rewards / Lottery Scams
    "reward",
    "cashback",
    "prize",
    "winner",
    "congratulations",
    "lucky draw",
    "lottery",
    "gift",
    "bonus",
    "free",
    "credited 30000.00",

    # Fake Support / Impersonation
    "customer care",
    "support team",
    "bank officer",
    "official team",
    "helpline",
    "refund team",

    # Suspicious Links
    "click here",
    "open link",
    "visit link",
    "http",
    "www",
    "bit.ly",
    "short link",

    # Scam Actions
    "share otp",
    "enter otp",
    "install app",
    "download app",
    "remote access",
    "screen share",
    "allow access",
    "anydesk", "rustdesk",


    "इनाम",
    "लॉटरी",
    "केवाईसी",
    "खाता बंद",
    "पैसे भेजें",
    "ओटीपी",
    "रिफंड",
    "जीत गए"
    

]


    score = 0


    text=text.lower()


    for word in keywords:

        if word in text:
            score +=1



    if score >=2:

        return {

            "status":"Scam Detected",

            "confidence":90,

            "risk":"High"

        }


    else:

        return {

            "status":"Safe",

            "confidence":80,

            "risk":"Low"

        }