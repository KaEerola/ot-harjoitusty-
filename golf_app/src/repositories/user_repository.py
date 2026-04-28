import sqlite3


class UserRepository:
    """Handles database operations related to users.

    This repository provides methods for creating users
    and retrieving user information from the database.
    """

    def __init__(self, db_file="golf.db"):
        """Initializes the repository with a database file.

        Args:
            db_file (str): Path to the SQLite database file.
        """
        self.db_file = db_file

    def create_user(self, username, password):
        """Creates a new user in the database.

        Args:
            username (str): Unique username.
            password (str): User's password.

        Returns:
            bool: True if user was created successfully,
                  False if the username already exists.
        """
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
        """Finds a user by username.

        Args:
            username (str): Username to search for.

        Returns:
            dict | None: A dictionary containing user data
            (id, username, password) if found, otherwise None.
        """
        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()
        cur.execute(
            "SELECT id, username, password FROM users WHERE username=?",
            (username,)
        )
        row = cur.fetchone()
        conn.close()

        if row:
            return {"id": row[0], "username": row[1], "password": row[2]}
        return None