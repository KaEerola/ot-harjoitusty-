import unittest
from datetime import date
from unittest.mock import MagicMock

from src.services.statistics_service import StatisticsService


class DummyRound:
    def __init__(self, score, date):
        self.score = score
        self.date = date


class TestStatisticsService(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock()
        self.mock_auth = MagicMock()
        self.mock_auth.current_user = {"id": 1}

        self.service = StatisticsService(self.mock_repo, self.mock_auth)

        self.rounds = [
            DummyRound(90, date(2024, 1, 1)),
            DummyRound(85, date(2024, 2, 1)),
            DummyRound(100, date(2024, 3, 1)),
        ]

        self.mock_repo.get_by_user.return_value = self.rounds

    def test_average_score(self):
        avg = self.service.average_score()
        self.assertEqual(avg, (90 + 85 + 100) / 3)

    def test_average_score_empty(self):
        self.mock_repo.get_by_user.return_value = []
        avg = self.service.average_score()
        self.assertIsNone(avg)

    def test_best_score(self):
        best = self.service.best_score()
        self.assertEqual(best, 85)

    def test_best_score_empty(self):
        self.mock_repo.get_by_user.return_value = []
        best = self.service.best_score()
        self.assertIsNone(best)

    def test_total_rounds(self):
        total = self.service.total_rounds()
        self.assertEqual(total, 3)

    def test_total_rounds_empty(self):
        self.mock_repo.get_by_user.return_value = []
        total = self.service.total_rounds()
        self.assertEqual(total, 0)

    def test_filter_by_date(self):
        filtered = self.service._filter_by_date(
            self.rounds,
            start_date=date(2024, 2, 1),
            end_date=date(2024, 3, 1)
        )
        self.assertEqual(len(filtered), 2)

    def test_average_score_with_date_filter(self):
        avg = self.service.average_score(
            start_date=date(2024, 2, 1)
        )
        self.assertEqual(avg, (85 + 100) / 2)

    def test_last_n_rounds(self):
        last_two = self.service.last_n_rounds(2)
        self.assertEqual(len(last_two), 2)
        self.assertEqual(last_two[0].date, date(2024, 3, 1))
        self.assertEqual(last_two[1].date, date(2024, 2, 1))

    def test_average_last_10_vs_all(self):
        last_10_avg, all_avg = self.service.average_last_10_vs_all()

        self.assertEqual(all_avg, (90 + 85 + 100) / 3)
        self.assertEqual(last_10_avg, all_avg) 

    def test_average_last_10_vs_all_empty(self):
        self.mock_repo.get_by_user.return_value = []

        last_10_avg, all_avg = self.service.average_last_10_vs_all()

        self.assertIsNone(last_10_avg)
        self.assertIsNone(all_avg)

    def test_filter_by_end_date_excludes_later_rounds(self):
        filtered = self.service._filter_by_date(
            self.rounds,
            start_date=None,
            end_date=date(2024, 2, 1)
        )

        self.assertEqual(len(filtered), 2)
        self.assertTrue(all(r.date <= date(2024, 2, 1) for r in filtered))


if __name__ == "__main__":
    unittest.main()