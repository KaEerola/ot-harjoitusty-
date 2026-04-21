import sqlite3

class UserRepository:
    def __init__(self, db_file="golf.db"):
        self.db_file = db_file

    def create_user(self, username, password):
        try:
            conn = sqlite3.connect(self.db_file)
            cur = conn.cursor()
            cur.execute(
                "INSERT INTO users (username, password) VALUES (?, ?)",
                (username, password)
            )
            conn.commit()
            conn.close()
            return True
        except sqlite3.IntegrityError:
            return False

    def find_by_username(self, username):
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()
        cur.execute("SELECT id, username, password FROM users WHERE username=?", (username,))
        row = cur.fetchone()
        conn.close()

        if row:
            return {"id": row[0], "username": row[1], "password": row[2]}
        return None