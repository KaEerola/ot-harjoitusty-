import unittest
from src.domain.round import Round

class TestRound(unittest.TestCase):

    def test_round_initialization(self):
        round_obj = Round("Helsinki Golf Club", 85)

        self.assertEqual(round_obj.course, "Helsinki Golf Club")
        self.assertEqual(round_obj.score, 85)