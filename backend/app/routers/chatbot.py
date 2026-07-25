from fastapi import APIRouter
from pydantic import BaseModel

from app.services.chatbot_service import generate_chat_response


router = APIRouter(
    prefix="/chatbot",
    tags=["AI Chat Assistant"]
)



class ChatRequest(BaseModel):

    message: str



@router.post("/chat")
async def chatbot(request: ChatRequest):

    response = await generate_chat_response(
        request.message
    )

    return response