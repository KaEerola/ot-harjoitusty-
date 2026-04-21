import sqlite3

class RoundRepository:
    def __init__(self, db_file="golf.db"):
        self.db_file = db_file

    def create(self, course, score, date, user_id):
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO rounds (course, score, date, user)
            VALUES (?, ?, ?, ?)
        """, (course, score, date, user_id))

        conn.commit()
        conn.close()

    def get_by_user(self, user_id):
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()

        cur.execute("""
            SELECT id, course, score, date, user
            FROM rounds
            WHERE user=?
        """, (user_id,))

        rows = cur.fetchall()
        conn.close()

        return rows

    def delete(self, round_id, user_id):
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()

        cur.execute("""
                    DELETE 
                    FROM rounds 
                    WHERE id=? AND user=?
                    """, (round_id, user_id))
        deleted_rows = cur.rowcount

        conn.commit()
        conn.close()

        return deleted_rows

    def update(self, round_id, course, score, date, user_id):
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()

        cur.execute("""
            UPDATE rounds
            SET course=?, score=?, date=?
            WHERE id=? AND user=?
        """, (course, score, date, round_id, user_id))

        conn.commit()
        conn.close()