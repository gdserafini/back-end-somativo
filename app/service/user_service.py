from app.models.user_model import User
import app.repository.user_repository as ur

async def get_user_by_id(user_id: int) -> User | None:
    if user_id is None or type(user_id) is not int or user_id <= 0: return None
    user_data = await ur.get_user_by_id(user_id)
    if user_data is None: return None
    return User(
        user_data['user_id'],
        user_data['username'],
        user_data['password'],
        user_data['email']
    )