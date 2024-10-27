from typing import Any
import mysql.connector
import json
import os

def get_connection() -> Any:
    base_dir = os.path.dirname(os.path.abspath(__file__))
    file_path = os.path.join(base_dir, 'db_config.json')
    with open(file_path, 'r') as db_config_file:
        db_config_data = json.load(db_config_file)
    try:
        connection = mysql.connector.connect(
            host=db_config_data['host'],
            user=db_config_data['user'],
            password=db_config_data['password'],
            database=db_config_data['database']
        )
        return connection
    except mysql.connector.Error as e:
        print(e)

