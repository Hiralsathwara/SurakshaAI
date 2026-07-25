from pydantic import BaseModel


class FAQItem(BaseModel):
    question: str
    answer: str


class FinancialLiteracyCategory(BaseModel):
    id: int
    title: str
    icon: str


class FinancialLiteracyTopicResponse(BaseModel):
    title: str
    faqs: list[FAQItem]
