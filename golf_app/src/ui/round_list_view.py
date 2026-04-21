import tkinter as tk
from tkinter import ttk, messagebox

class RoundListView:
    def __init__(self, root, service, on_add):
        self.service = service
        self.on_add = on_add

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
            text="Poista kierros",
            command=self.handle_delete
        ).pack(pady=10)

        self.refresh()

    def handle_delete(self):
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
        self.listbox.delete(0, tk.END)
        self.round_ids = []
        for r in self.service.get_rounds():
            self.round_ids.append(r[0])
            self.listbox.insert(
                tk.END,
                f"{r[1]} — {r[2]} — {r[3]}"
            )

    def destroy(self):
        self.frame.destroy()