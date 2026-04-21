from tkinter import ttk

class LoginView:
    def __init__(self, root, auth_service, on_login_success, on_show_register):
        self.auth = auth_service
        self.on_login_success = on_login_success
        self.on_show_register = on_show_register

        self.frame = ttk.Frame(root)
        self.frame.pack(fill="both", expand=True, padx=20, pady=20)

        ttk.Label(self.frame, text="Kirjaudu").pack(pady=10)

        self.username = ttk.Entry(self.frame)
        self.username.pack()

        self.password = ttk.Entry(self.frame, show="*")
        self.password.pack()

        ttk.Button(self.frame, text="Login", command=self.login).pack(pady=5)
        ttk.Button(self.frame, text="Register", command=self.on_show_register).pack()

        self.message = ttk.Label(self.frame, text="")
        self.message.pack()

    def login(self):
        if self.auth.login(self.username.get(), self.password.get()):
            self.on_login_success()
        else:
            self.message.config(text="Väärä käyttäjä tai salasana")

    def destroy(self):
        self.frame.destroy()