from tkinter import messagebox, ttk
from src.ui.utils.entry_utils import add_placeholder, clear_placeholder
from src.services.validation_service import validate_inputs


class AddRoundView:
    """UI view for adding a new golf round.

    This view provides input fields for course name, score,
    and date, validates the input, and delegates saving
    to the RoundService.
    """

    def __init__(self, root, service, on_back):
        """Initializes the add round view.

        Args:
            root (tk.Widget): Parent widget (typically Tk root).
            service (RoundService): Service used to add a new round.
            on_back (Callable): Callback function to return to the previous view.
        """
        self.service = service
        self.on_back = on_back

        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self.frame, text="Lisää kierros").pack(pady=10)

        self.course_entry = ttk.Entry(self.frame)
        self.course_entry.pack()
        add_placeholder(self.course_entry, "Kentän nimi")

        self.score_entry = ttk.Entry(self.frame)
        self.score_entry.pack()
        add_placeholder(self.score_entry, "Tulos (esim. 85)")

        self.date_entry = ttk.Entry(self.frame)
        self.date_entry.pack()
        add_placeholder(self.date_entry, "Päivämäärä (YYYY-MM-DD)")

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
        """Validates input and creates a new round.

        Reads values from input fields, validates them using
        ValidationService, and calls RoundService to save
        the round. Shows an error dialog if validation fails.
        """
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
        """Destroys the view and returns to the previous view."""
        self.frame.destroy()
        self.on_back()

    def destroy(self):
        """Destroys the view frame."""
        self.frame.destroy()