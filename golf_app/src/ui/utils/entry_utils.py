def add_placeholder(entry, text):
    """Adds placeholder text to an Entry widget and handles its display and hiding.
    Args:
        entry (str): The Entry widget.
        text (str): The placeholder text.
    """
    entry.insert(0, text)
    entry.config(foreground="gray")

    def on_focus_in(event):
        """Deletes the placeholder text when the Entry gains focus, if the current text is the placeholder.
        """
        if entry.get() == text:
            entry.delete(0, "end")
            entry.config(foreground="black")

    def on_focus_out(event):
        """Restores the placeholder text if the Entry loses focus and is empty.
        """
        if not entry.get():
            entry.insert(0, text)
            entry.config(foreground="gray")

    entry.bind("<FocusIn>", on_focus_in)
    entry.bind("<FocusOut>", on_focus_out)


def clear_placeholder(entry, placeholder):
    """Clears the placeholder text from an Entry widget.
    Args:
        entry (str): The Entry widget.
        placeholder (str): The placeholder text.
    Returns:
        str: The actual value from the Entry, or an empty string if it matches the placeholder
        """
    value = entry.get()
    return "" if value == placeholder else value