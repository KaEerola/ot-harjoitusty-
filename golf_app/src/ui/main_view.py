from tkinter import *
from src.ui.round_list_view import RoundListView
from src.ui.add_round_view import AddRoundView
from src.ui.stats_view import StatsView



class MainView:
    """Ui main view that manages navigation between different screens.
    """
    def __init__(self, root, auth_service, round_service, stats_service):
        """Initializes the main view and shows the round list view.

        Args:
            root (tk.Widget): Parent widget (typically Tk root).
            auth_service (AuthService): Service used for authentication.
            round_service (RoundService): Service used for managing rounds.
            stats_service (StatsService): Service used for managing statistics.
        """
        self.root = root
        self.service = round_service
        self.stats_service = stats_service
        self.current_view = None

        self.show_list_view()

    def clear_view(self):
        if self.current_view:
            self.current_view.destroy()

    def show_list_view(self):
        self.clear_view()
        self.current_view = RoundListView(
            self.root,
            self.service,
            on_add=self.show_add_view,
            on_stats=self.show_stats_view
        )

    def show_add_view(self):
        self.clear_view()
        self.current_view = AddRoundView(
            self.root,
            self.service,
            on_back=self.show_list_view
        )

    def show_stats_view(self):
        self.clear_view()
        self.current_view = StatsView(
            self.root,
            self.stats_service,
            on_back=self.show_list_view
        )
