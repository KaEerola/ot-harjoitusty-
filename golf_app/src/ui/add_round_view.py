from tkinter import messagebox, ttk
from src.services.validation_service import validate_inputs

class AddRoundView:
    def __init__(self, root, service, on_back):
        self.service = service
        self.on_back = on_back

        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self.frame, text="Lisää kierros").pack(pady=10)

        self.course_entry = ttk.Entry(self.frame)
        self.course_entry.pack()

        self.score_entry = ttk.Entry(self.frame)
        self.score_entry.pack()

        self.date_entry = ttk.Entry(self.frame)
        self.date_entry.pack()

        ttk.Button(
            self.frame,
            text="Tallenna",
            command=self.add_round
        ).pack(pady=10)

        ttk.Button(
            self.frame,
            text="Takaisin",
            command=self.on_back
        ).pack()

    def add_round(self):
        course = self.course_entry.get()
        score_input = self.score_entry.get()
        date_input = self.date_entry.get()

        try:
            course, score, date = validate_inputs(
                course, score_input, date_input
            )
        except ValueError as e:
            messagebox.showerror("Virhe", str(e))
            return

        self.service.add_round(course, score, date)

        self.on_back()

    def on_back(self):
        self.frame.destroy()
        self.on_back()
    
    def destroy(self):
        self.frame.destroy()