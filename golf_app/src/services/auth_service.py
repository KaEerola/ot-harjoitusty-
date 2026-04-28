class AuthService:
    """Handles user authentication and session management.

    This service provides functionality for registering users,
    logging in, logging out, and accessing the currently
    authenticated user.
    """

    def __init__(self, user_repository):
        """Initializes the authentication service.

        Args:
            user_repository (UserRepository): Repository for user data access.
        """
        self.user_repository = user_repository
        self.current_user = None

    def register(self, username, password):
        """Registers a new user.

        Args:
            username (str): Desired username.
            password (str): User's password.

        Returns:
            bool: True if input is valid (creation attempted),
                  False if username or password is empty.
        """
        if not username or not password:
            return False

        self.user_repository.create_user(username, password)
        return True

    def login(self, username, password):
        """Logs in a user with given credentials.

        Args:
            username (str): Username.
            password (str): Password.

        Returns:
            bool: True if login is successful, otherwise False.
        """
        if not username or not password:
            return False

        user = self.user_repository.find_by_username(username)

        if not user:
            return False

        if user["password"] == password:
            self.current_user = user
            return True

        return False

    def logout(self):
        """Logs out the current user."""
        self.current_user = None

    def get_current_user(self):
        """Returns the currently logged-in user.

        Returns:
            dict | None: Current user data, or None if no user is logged in.
        """
        return self.current_user
