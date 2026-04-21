import unittest
from unittest.mock import MagicMock
from src.services.round_service import RoundService


class TestRoundService(unittest.TestCase):

    def setUp(self):
        self.mock_auth = MagicMock()
        self.mock_repo = MagicMock()

        self.mock_auth.current_user = {"id": 1}

        self.service = RoundService(self.mock_auth, self.mock_repo)

    def test_add_round_calls_repo_with_correct_user(self):
        self.service.add_round("Helsinki Golf Club", 85, "2026-04-13")

        self.mock_repo.create.assert_called_once_with(
            "Helsinki Golf Club", 85, "2026-04-13", 1
        )

    def test_get_rounds_returns_repo_result(self):
        self.mock_repo.get_by_user.return_value = [
            (1, "Helsinki Golf Club", 85, "2026-04-13")
        ]

        rounds = self.service.get_rounds()

        self.mock_repo.get_by_user.assert_called_once_with(1)
        self.assertEqual(len(rounds), 1)

    def test_delete_round_success(self):
        self.mock_repo.delete.return_value = 1

        self.service.delete_round(1)

        self.mock_repo.delete.assert_called_once_with(1, 1)

    def test_delete_round_raises_permission_error(self):
        self.mock_repo.delete.return_value = 0

        with self.assertRaises(PermissionError):
            self.service.delete_round(1)

    def test_update_round_calls_repo(self):
        self.service.update_round(1, "Espoo Golf", 90, "2026-04-14")

        self.mock_repo.update.assert_called_once_with(
            1, "Espoo Golf", 90, "2026-04-14", 1
        )