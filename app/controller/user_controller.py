import app.service.user_service as us
from app.models.user_view import UserView
from fastapi import APIRouter

router = APIRouter()

@router.get('/user/{user_id}')
async def get_user(user_id: int) -> dict:
    user = await us.get_user_by_id(user_id)
    user_view = UserView(user)
    return user_view.get()
