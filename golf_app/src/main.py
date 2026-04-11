import tkinter as tk
from src.ui.main_view import MainView

def main():
    root = tk.Tk()
    MainView(root)
    root.mainloop()

if __name__ == "__main__":
    main()