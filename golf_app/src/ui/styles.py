from tkinter import ttk

def setup_styles():
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame", background="#a7f2d1")
    style.configure("TLabel", background="#a7f2d1", foreground="#333333")

    style.configure("Green.TButton", foreground="white", padding=6)

    return style