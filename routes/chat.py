from fastapi import APIRouter, Request
from services.chat_service import handle_user_query

router = APIRouter()

@router.post("/chat")
async def chat(request: Request):
    body = await request.json()
    user_input = body.get("message", "")
    return await handle_user_query(user_input)
