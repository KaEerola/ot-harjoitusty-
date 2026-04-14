import unittest
from src.services.round_service import RoundService

class TestRoundService(unittest.TestCase):

    def test_round_service_initialization(self):
        round_service = RoundService()

        self.assertIsNotNone(round_service)
    
    def test_add_round(self):
        round_service = RoundService()
        round_service.add_round("Helsinki Golf Club", 85, "2026-04-13")

        rounds = round_service.get_rounds()

        self.assertEqual(len(rounds), 1)
        self.assertEqual(rounds[0].course, "Helsinki Golf Club")
        self.assertEqual(rounds[0].score, 85)
        self.assertEqual(rounds[0].date, "2026-04-13")