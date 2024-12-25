import psycopg2
import os
from dotenv import load_dotenv

load_dotenv()

class DatabaseManager():
    def __init__(self):
        self.host = os.getenv("FSTR_DB_HOST")
        self.port = os.getenv("FSTR_DB_PORT")
        self.user = os.getenv("FSTR_DB_LOGIN")
        self.password = os.getenv("FSTR_DB_PASS")
        self.db_name = "pereval" 

    def connect(self):
        try:
            self.conn = psycopg2.connect(
                host = self.host, 
                port = self.port, 
                user = self.user, 
                password = self.password, 
                database = self.db_name
            )

            self.cursor = self.conn.cursor()
            print(f"соединение с базой данных {self.db_name} прошло успешно")
        except psycopg2.Error as e:
            print(f"Ошибка соединения с базой данных {e}")

    def close(self):
        if hasattr(self, 'conn') and self.conn:
           self.conn.close()
           print("Соединение с базой данных закрыто.")

    def add_user:
        

    
