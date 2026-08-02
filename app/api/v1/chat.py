from fastapi import APIRouter

from app.schemas.chat import ChatResponse
from app.schemas.chat import ChatRequest
from app.services.rag_service import RAGServcie

router = APIRouter()

@router.post("/chat",response_model=ChatResponse)
async def chat(request: ChatRequest):
    response = RAGServcie().ask(request.question)
    return ChatResponse(
        answer=response.answer,
        sources=response.sources
    )