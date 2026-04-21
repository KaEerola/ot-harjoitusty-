from tkinter import ttk

class RegisterView:
    def __init__(self, root, auth_service, on_success, on_back):
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
        success = self.auth.register(
            self.username.get(),
            self.password.get()
        )

        if success:
            self.on_success()
        else:
            self.message.config(text="Virhe tai käyttäjä on jo olemassa")

    def destroy(self):
        self.frame.destroy()