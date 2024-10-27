from app.repository.database import get_connection

async def get_user_by_id(user_id: int) -> tuple:
    connection = get_connection()
    try:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM user WHERE id = %s", (user_id,))
        user = cursor.fetchone()
        connection.close()
        return user
    except Exception as e:
        print(e)