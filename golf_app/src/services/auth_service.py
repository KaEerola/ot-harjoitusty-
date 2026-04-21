class AuthService:
    def __init__(self, user_repository):
        self.user_repository = user_repository
        self.current_user = None

    def register(self, username, password):
        if not username or not password:
            return False

        self.user_repository.create_user(username, password)
        return True

    def login(self, username, password):
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
        self.current_user = None

    def get_current_user(self):
        return self.current_user