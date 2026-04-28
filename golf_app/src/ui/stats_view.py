import tkinter as tk
from tkinter import ttk
from datetime import datetime

class StatsView:
    """UI view for displaying golf statistics.
    This view allows users to input a date range and calculates various statistics based on the recorded rounds. It also shows the last N rounds and compares the average of the last 10 rounds to the overall average.
    """
    def __init__(self, root, stats_service, on_back=None):
        """Initializes the statistics view. 

        Args:
            root (tk.Widget): Parent widget (typically Tk root).
            stats_service (StatsService): Service used for calculating statistics.
            on_back (Callable, optional): Callback function to navigate back. Defaults to None.
        """
        self.service = stats_service
        self.on_back = on_back

        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self.frame, text="Tilastot").pack(pady=10)

        ttk.Label(self.frame, text="Alkupäivä (YYYY-MM-DD)").pack()
        self.start_entry = ttk.Entry(self.frame)
        self.start_entry.pack(pady=2)

        ttk.Label(self.frame, text="Loppupäivä (YYYY-MM-DD)").pack()
        self.end_entry = ttk.Entry(self.frame)
        self.end_entry.pack(pady=2)

        ttk.Button(
            self.frame,
            text="Laske tilastot",
            command=self._calculate
        ).pack(pady=10)

        ttk.Label(self.frame, text="Viimeiset kierrokset").pack(pady=5)

        self.n_var = tk.StringVar(value="5")

        self.n_select = ttk.Combobox(
            self.frame,
            textvariable=self.n_var,
            values=["5", "10", "15", "20"],
            state="readonly"
        )
        self.n_select.pack(pady=5)
        self.n_select.bind("<<ComboboxSelected>>", lambda e: self._update_last_n())

        self.lastn_label = ttk.Label(self.frame, text="Viime kierrokset: -")
        self.lastn_label.pack(pady=5)

        self.avg_label = ttk.Label(self.frame, text="Keskiarvo: -")
        self.avg_label.pack(pady=5)

        self.best_label = ttk.Label(self.frame, text="Paras tulos: -")
        self.best_label.pack(pady=5)

        self.count_label = ttk.Label(self.frame, text="Kierroksia: -")
        self.count_label.pack(pady=5)

        self.comp_label = ttk.Label(self.frame, text="Viime 10 vs kaikki: -")
        self.comp_label.pack(pady=5)

        if self.on_back:
            ttk.Button(
                self.frame,
                text="Takaisin",
                command=self.on_back
            ).pack(pady=10)

        self._update_last_n()

    def _parse_date(self, value):
        """Parses a date string into a date object.

        Args:
            value (str): Date string in the format YYYY-MM-DD.

        Returns:
            datetime.date: Date object.
        """
        if not value.strip():
            return None
        return datetime.strptime(value, "%Y-%m-%d").date()

    def _calculate(self):
        """Calculates and updates the statistics based on the input date range. Fetches average score, best score, total rounds, and comparison of last 10 rounds to overall average from the service. Updates the corresponding labels with the calculated values. Handles any exceptions that may occur during calculation, such as invalid date formats.
        """
        try:
            start = self._parse_date(self.start_entry.get())
            end = self._parse_date(self.end_entry.get())

            avg = self.service.average_score(start, end)
            best = self.service.best_score(start, end)
            count = self.service.total_rounds(start, end)

            last10, all_avg = self.service.average_last_10_vs_all()

            self.avg_label.config(
                text=f"Keskiarvo: {avg:.1f}" if avg else "Keskiarvo: -"
            )

            self.best_label.config(
                text=f"Paras: {best}" if best else "Paras: -"
            )

            self.count_label.config(text=f"Kierroksia: {count}")

            self.comp_label.config(
                text=f"Viime 10: {last10:.1f} | Kaikki: {all_avg:.1f}"
                if last10 and all_avg else "Viime 10 vs kaikki: -"
            )

        except ValueError:
            self.avg_label.config(text="Virhe päivämäärässä")
        
    def _update_last_n(self):
        """Updates the label showing the last N rounds based on the selected value in the combobox. Fetches the last N rounds from the service and updates the label text. Handles any exceptions that may occur during fetching.
        """
        try:
            n = int(self.n_var.get())
            rounds = self.service.last_n_rounds(n)

            text = "Viime " + str(n) + ": " + ", ".join(
                str(r.score) for r in rounds
            )

            self.lastn_label.config(text=text)

        except Exception as e:
            self.lastn_label.config(text=f"Virhe: {e}")

    def destroy(self):
        """Destroys the view frame and calls the back callback if provided.
        """
        self.frame.destroy()
