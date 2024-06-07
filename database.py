# Pip and Virtualenv
from data import Database


def db():
    service = input(f"""
        1. Users
            >>> """)

    if service == "1":
        query = "SELECT * FROM users"
        print(*Database.connect(query, "select"), sep="\n")



if __name__ == "__main__":
    db()
