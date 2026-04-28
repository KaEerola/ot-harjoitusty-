import unittest
from unittest.mock import MagicMock
from src.services.auth_service import AuthService


class TestAuthService(unittest.TestCase):

    def setUp(self):
        self.mock_repo = MagicMock()
        self.auth_service = AuthService(self.mock_repo)

    def test_register_success(self):
        result = self.auth_service.register("user1", "pass123")

        self.assertTrue(result)
        self.mock_repo.create_user.assert_called_once_with("user1", "pass123")

    def test_register_missing_username(self):
        result = self.auth_service.register("", "pass123")

        self.assertFalse(result)
        self.mock_repo.create_user.assert_not_called()

    def test_register_missing_password(self):
        result = self.auth_service.register("user1", "")

        self.assertFalse(result)
        self.mock_repo.create_user.assert_not_called()

    def test_login_success(self):
        self.mock_repo.find_by_username.return_value = {
            "username": "user1",
            "password": "pass123"
        }

        result = self.auth_service.login("user1", "pass123")

        self.assertTrue(result)
        self.assertEqual(self.auth_service.get_current_user()["username"], "user1")
        self.mock_repo.find_by_username.assert_called_once_with("user1")

    def test_login_user_not_found(self):
        self.mock_repo.find_by_username.return_value = None

        result = self.auth_service.login("user1", "pass123")

        self.assertFalse(result)
        self.assertIsNone(self.auth_service.get_current_user())

    def test_login_wrong_password(self):
        self.mock_repo.find_by_username.return_value = {
            "username": "user1",
            "password": "wrong"
        }

        result = self.auth_service.login("user1", "pass123")

        self.assertFalse(result)
        self.assertIsNone(self.auth_service.get_current_user())

    def test_login_missing_fields(self):
        self.assertFalse(self.auth_service.login("", "pass123"))
        self.assertFalse(self.auth_service.login("user1", ""))

    def test_logout(self):
        self.auth_service.current_user = {"username": "user1"}

        self.auth_service.logout()

        self.assertIsNone(self.auth_service.get_current_user())


if __name__ == "__main__":
    unittest.main()