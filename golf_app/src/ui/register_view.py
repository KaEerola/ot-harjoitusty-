from tkinter import ttk

class RegisterView:
    """UI view for user registration.
    """
    def __init__(self, root, auth_service, on_success, on_back):
        """Initializes the registration view.
        Args:
            root (tk.Widget): Parent widget (typically Tk root).
            auth_service (AuthService): Service used for authentication.
            on_success (Callable): Callback function for successful registration.
            on_back (Callable): Callback function to return to the previous view.
        """
        self.auth = auth_service
        self.on_success = on_success
        self.on_back = on_back

        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self.frame, text="Rekisteröidy").pack(pady=10)

        self.username = ttk.Entry(self.frame)
        self.username.pack()

        self.password = ttk.Entry(self.frame, show="*")
        self.password.pack()

        ttk.Button(self.frame, text="Luo käyttäjä", command=self.register).pack(pady=5)
        ttk.Button(self.frame, text="Takaisin", command=self.on_back).pack()

        self.message = ttk.Label(self.frame, text="")
        self.message.pack()

    def register(self):
        """Validates input and attempts to register the user.
        """
        if not self.username.get() or not self.password.get():
            self.message.config(text="Kaikki kentät ovat pakollisia")
            return

        success = self.auth.register(
            self.username.get(),
            self.password.get()
        )

        if success:
            self.on_success()
        else:
            self.message.config(text="Virhe tai käyttäjä on jo olemassa")

    def destroy(self):
        """Destroys the view frame.
        """
        self.frame.destroy()