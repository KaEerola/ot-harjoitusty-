import tkinter as tk
from tkinter import ttk, messagebox

class RoundListView:
    """UI view for displaying the list of golf rounds.
    This view shows all recorded rounds in a listbox and provides
    buttons to add a new round, view statistics, and delete selected rounds.
    """
    def __init__(self, root, service, on_add, on_stats):
        """Initializes the round list view.

        Args:
            root (tk.Widget): Parent widget (typically Tk root).
            service (RoundService): Service used for managing rounds.
            on_add (Callable): Callback function to navigate to the add round view.
            on_stats (Callable): Callback function to navigate to the statistics view.
        """
        self.service = service
        self.on_add = on_add
        self.on_stats = on_stats

        self.round_ids = []

        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self.frame, text="Kierrokset").pack(pady=10)

        self.listbox = tk.Listbox(self.frame, width=50)
        self.listbox.pack(fill="both", expand=True, pady=10)

        ttk.Button(
            self.frame,
            text="Lisää kierros",
            command=self.on_add
        ).pack(pady=10)

        ttk.Button(
            self.frame,
            text="Tilastot",
            command=self.on_stats
        ).pack(pady=10)

        ttk.Button(
            self.frame,
            text="Poista kierros",
            command=self.handle_delete
        ).pack(pady=10)

        self.refresh()

    def handle_delete(self):
        """Handles the deletion of a selected round.
         Checks if a round is selected, confirms deletion with the user, and calls the service to delete the round. Refreshes the list after deletion.
         Shows error messages if no round is selected or if deletion fails.
        """
        selection = self.listbox.curselection()

        if not selection:
            messagebox.showerror("Virhe", "Valitse kierros")
            return

        index = selection[0]
        round_id = self.round_ids[index]

        if not messagebox.askyesno("Vahvistus", "Poistetaanko kierros?"):
            return

        try:
            self.service.delete_round(round_id)
            self.refresh()
        except Exception as e:
            messagebox.showerror("Virhe", str(e))

    def refresh(self):
        """Refreshes the list of rounds displayed in the listbox.
         Fetches the latest rounds from the service and updates the listbox.
         Also updates the internal list of round IDs for reference when deleting.
        """
        self.listbox.delete(0, tk.END)
        self.round_ids = []
        for r in self.service.get_rounds():
            self.round_ids.append(r.id)
            self.listbox.insert(
                tk.END,
                f"{r.course} — {r.score} — {r.date}"
            )

    def destroy(self):
        """Destroys the view frame.
        """
        self.frame.destroy()