import os
from dotenv import load_dotenv
import psycopg2 as psql
load_dotenv()

class Database:
    @staticmethod
    def connect(query: str, query_type: str):
        db = psql.connect(
            database=os.getenv("n44"),
            user=os.getenv("postgres"),
            password=os.getenv("1102"),
            host=os.getenv("localhost"),
            port=os.getenv("5432")
        )

        cursor = db.cursor()
        cursor.execute(query)
        data = ["update", "insert", "delete", "alter"]   # select
        if query_type in data:
            db.commit()
            if query_type == "update":
                return "updated data"

            elif query_type == "insert":
                return "inserted data"

            elif query_type == "delete":
                return "deleted data"

            elif query_type == "alter":
                return "alter data"

        else:
            return cursor.fetchall()