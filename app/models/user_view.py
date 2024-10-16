from app.models.user_model import User

class UserView:
    def __init__(self, user: User):
        self._user = user

    def get(self) -> dict:
        return {
            'user_id': str(self._user.get_id()),
            'username': self._user.get_username(),
            'email': self._user.get_email()
        }