# password generator
import tkinter as tk
from tkinter import ttk, messagebox
import random
import string

class PasswordGeneratorApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")

        self.password_var = tk.StringVar()
        self.password_length_var = tk.StringVar(value="12")  # Default password length

        # Create and set up the main frame
        main_frame = ttk.Frame(self.root, padding="20")
        main_frame.grid(row=0, column=0, sticky=(tk.W, tk.E, tk.N, tk.S))

        # Widgets
        ttk.Label(main_frame, text="Password Length:").grid(row=0, column=0, sticky=tk.W)
        length_entry = ttk.Entry(main_frame, textvariable=self.password_length_var, width=5)
        length_entry.grid(row=0, column=1, sticky=tk.W)
        ttk.Button(main_frame, text="Generate Password", command=self.generate_password).grid(row=1, column=0, columnspan=2, pady=10)
        ttk.Entry(main_frame, textvariable=self.password_var, state="readonly", width=30, font=("Courier", 12)).grid(row=2, column=0, columnspan=2, pady=10)

    def generate_password(self):
        try:
            password_length = int(self.password_length_var.get())
            if password_length <= 0:
                messagebox.showwarning("Invalid Length", "Please enter a positive integer for the password length.")
                return

            characters = string.ascii_letters + string.digits + string.punctuation
            password = ''.join(random.choice(characters) for _ in range(password_length))
            self.password_var.set(password)
        except ValueError:
            messagebox.showwarning("Invalid Length", "Please enter a valid integer for the password length.")

if __name__ == "__main__":
    root = tk.Tk()
    app = PasswordGeneratorApp(root)
    root.mainloop()
