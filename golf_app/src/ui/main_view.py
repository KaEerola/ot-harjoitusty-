from tkinter import *
from tkinter import messagebox
from src.services.round_service import RoundService
from src.services.validation_service import validate_inputs
from datetime import date, datetime

class MainView:
    def __init__(self, root):
        self.service = RoundService()

        # Kentät
        self.course_entry = Entry(root)
        self.course_entry.pack()

        self.score_entry = Entry(root)
        self.score_entry.pack()

        self.date_entry = Entry(root)  # uusi kenttä
        self.date_entry.pack()

        Button(root, text="Lisää", command=self.add_round).pack()

        self.listbox = Listbox(root)
        self.listbox.pack()

    def add_round(self):
        course = self.course_entry.get()
        score_input = self.score_entry.get()
        date_input = self.date_entry.get()

        try:
            course, score, date_input = validate_inputs(
                course, score_input, date_input
            )
        except ValueError as e:
            messagebox.showerror("Virhe", str(e))
            return

        self.service.add_round(course, score, date_input)
        self.refresh()

        self.course_entry.delete(0, END)
        self.score_entry.delete(0, END)
        self.date_entry.delete(0, END)

    def refresh(self):
        self.listbox.delete(0, END)
        for r in self.service.get_rounds():
            self.listbox.insert(END, f"{r.course} — {r.score} — {r.date}")