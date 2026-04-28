import sqlite3
from datetime import datetime
from src.domain.round import Round


class RoundRepository:
    """Handles database operations related to golf rounds.

    This repository provides methods to create, retrieve,
    update, and delete rounds stored in an SQLite database.
    """

    def __init__(self, db_file="golf.db"):
        """Initializes the repository with a database file.

        Args:
            db_file (str): Path to the SQLite database file.
        """
        self.db_file = db_file

    def _connect(self):
        """Creates a new database connection.

        Returns:
            sqlite3.Connection: A connection to the SQLite database.
        """
        return sqlite3.connect(self.db_file)

    def create(self, course, score, date, user_id):
        """Inserts a new round into the database.

        Args:
            course (str): Name of the golf course.
            score (int): Player's score.
            date (str): Date of the round (format: "YYYY-MM-DD").
            user_id (int): ID of the user who played the round.
        """
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            INSERT INTO rounds (course, score, date, user)
            VALUES (?, ?, ?, ?)
        """, (course, score, date, user_id))

        conn.commit()
        conn.close()

    def get_by_user(self, user_id):
        """Retrieves all rounds for a specific user.

        Args:
            user_id (int): ID of the user.

        Returns:
            list[Round]: A list of Round objects ordered by date (newest first).
        """
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            SELECT id, course, score, date, user
            FROM rounds
            WHERE user=?
            ORDER BY date DESC
        """, (user_id,))

        rows = cur.fetchall()
        conn.close()

        rounds = []

        for row in rows:
            rounds.append(
                Round(
                    row[0],
                    row[1],
                    row[2],
                    datetime.strptime(row[3], "%Y-%m-%d").date(),
                    row[4]
                )
            )

        return rounds

    def delete(self, round_id, user_id):
        """Deletes a round belonging to a specific user.

        Args:
            round_id (int): ID of the round to delete.
            user_id (int): ID of the user (ensures ownership).

        Returns:
            int: Number of deleted rows (0 or 1).
        """
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            DELETE FROM rounds 
            WHERE id=? AND user=?
        """, (round_id, user_id))

        deleted_rows = cur.rowcount

        conn.commit()
        conn.close()

        return deleted_rows

    def update(self, round_id, course, score, date, user_id):
        """Updates an existing round.

        Args:
            round_id (int): ID of the round to update.
            course (str): Updated course name.
            score (int): Updated score.
            date (str): Updated date (format: "YYYY-MM-DD").
            user_id (int): ID of the user (ensures ownership).
        """
        conn = self._connect()
        cur = conn.cursor()

        cur.execute("""
            UPDATE rounds
            SET course=?, score=?, date=?
            WHERE id=? AND user=?
        """, (course, score, date, round_id, user_id))

        conn.commit()
        conn.close()
        