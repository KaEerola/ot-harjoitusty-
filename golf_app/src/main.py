import tkinter as tk
from src.services.auth_service import AuthService
from src.services.round_service import RoundService
from src.repositories.user_repository import UserRepository
from src.ui.login_view import LoginView
from src.ui.register_view import RegisterView
from src.ui.main_view import MainView
from src.ui.styles import setup_styles
from src.database.db import init_db
from src.repositories.round_repository import RoundRepository

class App:
    def __init__(self, root):
        self.root = root

        init_db()

        self.user_repo = UserRepository()
        self.auth = AuthService(self.user_repo)

        self.round_repo = RoundRepository()
        self.round_service = RoundService(self.auth, self.round_repo)

        self.current_view = None
        self.show_login()

    def clear_view(self):
        if self.current_view:
            self.current_view.destroy()

    def show_login(self):
        self.clear_view()
        self.current_view = LoginView(
            self.root,
            self.auth,
            on_login_success=self.show_main,
            on_show_register=self.show_register
        )

    def show_register(self):
        self.clear_view()
        self.current_view = RegisterView(
            self.root,
            self.auth,
            on_success=self.show_login,
            on_back=self.show_login
        )

    def show_main(self):
        self.clear_view()
        self.current_view = MainView(self.root, self.auth, self.round_service)


def main():
    root = tk.Tk()
    root.title("Golf App")
    setup_styles()

    App(root)

    root.mainloop()


if __name__ == "__main__":
    main()