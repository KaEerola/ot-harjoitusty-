import unittest
import os
import sqlite3
from src.repositories.round_repository import RoundRepository
from datetime import date, datetime

class TestRoundRepository(unittest.TestCase):

    def setUp(self):
        self.db_file = "test_golf.db"
        self.repo = RoundRepository(self.db_file)

        conn = sqlite3.connect(self.db_file)
        cur = conn.cursor()

        cur.execute("""
            CREATE TABLE IF NOT EXISTS rounds (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                course TEXT,
                score INTEGER,
                date TEXT,
                user INTEGER
            )
        """)

        conn.commit()
        conn.close()

    def tearDown(self):
        os.remove(self.db_file)

    def test_create_round(self):
        self.repo.create("Helsinki Golf Club", 85, "2026-04-13", 1)

        rounds = self.repo.get_by_user(1)

        self.assertEqual(len(rounds), 1)
        self.assertEqual(rounds[0].course, "Helsinki Golf Club")
        self.assertEqual(rounds[0].score, 85)
        self.assertEqual(rounds[0].date, date(2026, 4, 13))
        self.assertEqual(rounds[0].user_id, 1)

    def test_delete_round(self):
        self.repo.create("Helsinki Golf Club", 85, "2026-04-13", 1)
        rounds = self.repo.get_by_user(1)
        round_id = rounds[0].id

        deleted = self.repo.delete(round_id, 1)

        self.assertEqual(deleted, 1)
        self.assertEqual(len(self.repo.get_by_user(1)), 0)

    def test_get_by_user(self):
        self.repo.create("Helsinki Golf Club", 85, "2026-04-13", 1)
        self.repo.create("Espoo Golf", 90, "2026-04-14", 1)
        self.repo.create("Vantaa Golf", 80, "2026-04-15", 2)

        rounds_user_1 = self.repo.get_by_user(1)
        rounds_user_2 = self.repo.get_by_user(2)

        self.assertEqual(len(rounds_user_1), 2)
        self.assertEqual(len(rounds_user_2), 1)