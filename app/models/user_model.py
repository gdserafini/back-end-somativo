class User:
    def __init__(self,
                 user_id: int, username: str,
                 password: str, email: str) -> None:
        self._user_id = user_id
        self._username = username
        self._password = password
        self._email = email

    def __str__(self):
        return f'User id: {self._user_id}\nUsername: {self._username}'

    def __eq__(self, other):
        if isinstance(other, User):
            return (
                self._user_id == other._user_id and
                self._username == other._username and
                self._password == other._password and
                self._email == other._email
            )

    def get_id(self): return self._user_id
    def get_username(self): return self._username
    def get_password(self): return self._password
    def get_email(self): return self._email