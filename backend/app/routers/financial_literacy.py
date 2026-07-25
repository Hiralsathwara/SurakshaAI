from fastapi import APIRouter, HTTPException, status

from app.schemas.financial import (
    FAQItem,
    FinancialLiteracyCategory,
    FinancialLiteracyTopicResponse,
)

router = APIRouter(prefix="/financial-literacy", tags=["Financial Literacy"])


CATEGORIES = [
    {"id": 1, "title": "OTP Safety", "icon": "🔐"},
    {"id": 2, "title": "UPI Safety", "icon": "📱"},
    {"id": 3, "title": "Phishing Awareness", "icon": "🎣"},
    {"id": 4, "title": "Banking Safety", "icon": "🏦"},
    {"id": 5, "title": "Investment Scam Awareness", "icon": "💰"},
    {"id": 6, "title": "Scam Call Awareness", "icon": "📞"},
]

TOPICS = {
    1: {
        "title": "OTP Safety",
        "faqs": [
            {
                "question": "What is OTP?",
                "answer": "OTP (One-Time Password) is a temporary security code used to verify your identity during online transactions, login, and payments.",
            },
            {
                "question": "Can a bank employee ask for my OTP?",
                "answer": "No. Banks never ask for your OTP, UPI PIN, ATM PIN, CVV, or password.",
            },
            {
                "question": "What should I do if someone asks for OTP?",
                "answer": "Do not share it. End the call or chat immediately and report the suspicious activity.",
            },
        ],
    },
    2: {
        "title": "UPI Safety",
        "faqs": [
            {
                "question": "What is UPI?",
                "answer": "UPI (Unified Payments Interface) allows instant digital payments through apps like Google Pay, PhonePe, Paytm, and bank apps.",
            },
            {
                "question": "Is receiving money through UPI safe?",
                "answer": "Yes. You do not need to enter your UPI PIN to receive money. If anyone asks you to enter your PIN to receive money, it is a scam.",
            },
            {
                "question": "What is a UPI Collect Request?",
                "answer": "A collect request asks you to approve a payment. Always check the receiver name and amount before approving any unknown request.",
            },
        ],
    },
    3: {
        "title": "Phishing Awareness",
        "faqs": [
            {
                "question": "What is phishing?",
                "answer": "Phishing is a scam where criminals use fake websites, emails, messages, or apps to steal personal or financial information.",
            },
            {
                "question": "How can I identify phishing messages?",
                "answer": "Be careful of urgent threats, unknown links, fake rewards, and spelling mistakes in messages or emails.",
            },
        ],
    },
    4: {
        "title": "Banking Safety",
        "faqs": [
            {
                "question": "Should I share my banking details?",
                "answer": "Never share your ATM PIN, UPI PIN, OTP, password, or CVV with anyone, including callers claiming to be from your bank.",
            },
            {
                "question": "What should I do if money is stolen?",
                "answer": "Immediately call your bank, block your card or account, call the Cyber Crime Helpline at 1930, and report the fraud on the cybercrime portal.",
            },
        ],
    },
    5: {
        "title": "Investment Scam Awareness",
        "faqs": [
            {
                "question": "What are investment scams?",
                "answer": "Investment scams promise guaranteed returns, double money, fake trading apps, or easy crypto profits to trick people into losing money.",
            },
            {
                "question": "How can I stay safe?",
                "answer": "Verify company details, avoid guaranteed profit offers, and research carefully before investing.",
            },
        ],
    },
    6: {
        "title": "Scam Call Awareness",
        "faqs": [
            {
                "question": "How do scammers trick people?",
                "answer": "They often use fake KYC updates, bank verification calls, lottery offers, job scams, and loan scams to collect your personal information.",
            },
            {
                "question": "What should I do during suspicious calls?",
                "answer": "Do not share personal information, do not install unknown apps, and do not click unknown links.",
            },
        ],
    },
}


@router.get("/categories", response_model=list[FinancialLiteracyCategory])
def get_categories():
    return [FinancialLiteracyCategory(**item) for item in CATEGORIES]


@router.get("/topic/{topic_id}", response_model=FinancialLiteracyTopicResponse)
def get_topic(topic_id: int):
    topic = TOPICS.get(topic_id)
    if not topic:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="Topic not found",
        )

    return FinancialLiteracyTopicResponse(
        title=topic["title"],
        faqs=[FAQItem(**faq) for faq in topic["faqs"]],
    )
