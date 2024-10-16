import pandas as pd
import os

async def get_user_by_id(user_id: int) -> pd.DataFrame.iloc:
    current_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(current_dir, 'users.csv')
    df = pd.read_csv(file_path)
    user_row = df.loc[df['user_id'] == user_id]
    if user_row.empty: return None
    return user_row.iloc[0]