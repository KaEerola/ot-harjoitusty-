from tkinter import *
from src.ui.round_list_view import RoundListView
from src.ui.add_round_view import AddRoundView



class MainView:
    def __init__(self, root, auth_service, round_service):
        self.root = root
        self.service = round_service
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
            on_add=self.show_add_view
        )

    def show_add_view(self):
        self.clear_view()
        self.current_view = AddRoundView(
            self.root,
            self.service,
            on_back=self.show_list_view
        )
