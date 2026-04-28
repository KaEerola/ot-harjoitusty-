import tkinter as tk
from src.services.auth_service import AuthService
from src.services.round_service import RoundService
from src.services.statistics_service import StatisticsService
from src.repositories.user_repository import UserRepository
from src.ui.login_view import LoginView
from src.ui.register_view import RegisterView
from src.ui.main_view import MainView
from src.ui.styles import setup_styles
from src.database.db import init_db
from src.repositories.round_repository import RoundRepository

class App:
    """UI application class that manages the overall application flow 
    Includes authentication and navigation between views. 
    """
    def __init__(self, root):
        """Initializes the application, sets up the database, repositories, services, 
        and shows the login view.

        Args:
            root (tk.Tk): The root window for the application.
        """
        self.root = root

        init_db()

        self.user_repo = UserRepository()
        self.auth = AuthService(self.user_repo)

        self.round_repo = RoundRepository()
        self.round_service = RoundService(self.auth, self.round_repo)

        self.stats_service = StatisticsService(self.round_repo, self.auth)

        self.current_view = None
        self.show_login()

    def clear_view(self):
        """Clears the current view.
        """
        if self.current_view:
            self.current_view.destroy()

    def show_login(self):
        """Shows the login view. 
        Initializes the LoginView with the authentication service and sets it as the current view. 
        Provides callbacks for successful login and showing the registration view.
        """
        self.clear_view()
        self.current_view = LoginView(
            self.root,
            self.auth,
            on_login_success=self.show_main,
            on_show_register=self.show_register
        )

    def show_register(self):
        """Shows the registration view. 
        Initializes RegisterView with the authentication service and sets it as the current view. 
        Provides callbacks for successful registration and going back to the login view.
        """
        self.clear_view()
        self.current_view = RegisterView(
            self.root,
            self.auth,
            on_success=self.show_login,
            on_back=self.show_login
        )

    def show_main(self):
        """Shows the main view of the application after successful login. 
        Initializes the MainView with the necessary services and sets it as the current view.
        """
        self.clear_view()
        self.current_view = MainView(self.root, self.auth, self.round_service, self.stats_service)


def main():
    """Runs the application
    """
    root = tk.Tk()
    root.title("Golf App")
    root.tk.call("tk", "scaling", 1.2)
    setup_styles()

    App(root)

    root.mainloop()


if __name__ == "__main__":
    main()
