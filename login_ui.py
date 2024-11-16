import tkinter as tk
from tkinter import messagebox


class MainApp(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("User Authentication System")
        self.geometry("400x300")  # Set the window size

        # Container for all views (frames)
        self.container = tk.Frame(self)
        self.container.pack(fill="both", expand=True)

        # Dictionary to store frames (views)
        self.frames = {}

        # Initialize views
        for F in (LoginPage, RegistrationPage):
            frame = F(self.container, self)
            self.frames[F] = frame
            frame.grid(row=0, column=0, sticky="nsew")

        # Show the login page by default
        self.show_frame(LoginPage)

    def show_frame(self, page):
        """Raise the given frame to the top."""
        frame = self.frames[page]
        frame.tkraise()


class LoginPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Username label and entry
        tk.Label(self, text="Username").pack(pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        # Password label and entry
        tk.Label(self, text="Password").pack(pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Login button
        tk.Button(self, text="Login", command=self.login).pack(pady=20)

        # Navigate to registration page
        tk.Button(self, text="Register", command=lambda: controller.show_frame(RegistrationPage)).pack()

    def login(self):
        """Handle login logic here."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Attempting login for {username} with password {password}")
        # Replace with API calls or backend logic
        if username == "player" and password == "1234":  # Example validation
            messagebox.showinfo("Success", "Login successful!")
        else:
            messagebox.showerror("Error", "Invalid username or password")


class RegistrationPage(tk.Frame):
    def __init__(self, parent, controller):
        super().__init__(parent)

        # Username label and entry
        tk.Label(self, text="Username").pack(pady=10)
        self.username_entry = tk.Entry(self)
        self.username_entry.pack(pady=5)

        # Password label and entry
        tk.Label(self, text="Password").pack(pady=10)
        self.password_entry = tk.Entry(self, show="*")
        self.password_entry.pack(pady=5)

        # Register button
        tk.Button(self, text="Register", command=self.register).pack(pady=20)

        # Navigate back to login page
        tk.Button(self, text="Back to Login", command=lambda: controller.show_frame(LoginPage)).pack()

    def register(self):
        """Handle registration logic here."""
        username = self.username_entry.get()
        password = self.password_entry.get()
        print(f"Registering {username} with password {password}")
        # Replace with API calls or backend logic
        if username and password:  # Example validation
            messagebox.showinfo("Success", "Registration successful!")
        else:
            messagebox.showerror("Error", "Please fill in all fields")


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()
