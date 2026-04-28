from tkinter import ttk

def setup_styles():
    """Sets up the styles for the application using ttk.Style.
    
        Configures the theme and styles for frames, labels, and buttons to create a consistent look and feel across the application.
    
        Returns:
            ttk.Style: The configured style object.
    """
    style = ttk.Style()
    style.theme_use("clam")

    style.configure("TFrame", background="#a7f2d1")
    style.configure("TLabel", background="#a7f2d1", foreground="#333333")

    style.configure("Green.TButton", foreground="white", padding=6)

    return style