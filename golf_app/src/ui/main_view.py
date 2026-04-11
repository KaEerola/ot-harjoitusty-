from tkinter import *
from src.services.round_service import RoundService

class MainView:
    def __init__(self, root):
        self.service = RoundService()

        self.course_entry = Entry(root)
        self.course_entry.pack()

        self.score_entry = Entry(root)
        self.score_entry.pack()

        Button(root, text="Lisää", command=self.add_round).pack()

        self.listbox = Listbox(root)
        self.listbox.pack()

    def add_round(self):
        course = self.course_entry.get()
        score = int(self.score_entry.get())

        self.service.add_round(course, score)

        self.refresh()

    def refresh(self):
        self.listbox.delete(0, END)
        for r in self.service.get_rounds():
            self.listbox.insert(END, f"{r.course} — {r.score}")