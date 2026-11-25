
import tkinter as tk
from tkinter import messagebox
import subprocess
import sys
import os

# ------------------ LOGIN SETTINGS ------------------

BG = "#111318"
CARD = "#202631"
GOLD = "#D4AF37"
WHITE = "#FFFFFF"
MUTED = "#AAB0BC"

# Demo administrator account
ADMIN_USERNAME = "admin"
ADMIN_PASSWORD = "admin123"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))


# ------------------ LOGIN WINDOW ------------------

root = tk.Tk()
root.title("Admin Login - Student Management System")
root.geometry("450x550")
root.resizable(False, False)
root.configure(bg=BG)

# Main login card
login_frame = tk.Frame(
    root,
    bg=CARD,
    padx=40,
    pady=35
)
login_frame.place(
    relx=0.5,
    rely=0.5,
    anchor="center",
    width=370,
    height=440
)

# Logo / heading
tk.Label(
    login_frame,
    text="SMS",
    bg=CARD,
    fg=GOLD,
    font=("Arial", 32, "bold")
).pack(pady=(5, 0))

tk.Label(
    login_frame,
    text="STUDENT MANAGEMENT SYSTEM",
    bg=CARD,
    fg=WHITE,
    font=("Arial", 11, "bold")
).pack(pady=5)

tk.Label(
    login_frame,
    text="ADMINISTRATOR LOGIN",
    bg=CARD,
    fg=GOLD,
    font=("Arial", 10, "bold")
).pack(pady=(15, 20))


# ------------------ USERNAME ------------------

tk.Label(
    login_frame,
    text="Username",
    bg=CARD,
    fg=WHITE,
    font=("Arial", 10)
).pack(anchor="w")

username_entry = tk.Entry(
    login_frame,
    bg=BG,
    fg=WHITE,
    insertbackground=WHITE,
    font=("Arial", 11),
    bd=0
)
username_entry.pack(fill="x", pady=(7, 18), ipady=10)


# ------------------ PASSWORD ------------------

tk.Label(
    login_frame,
    text="Password",
    bg=CARD,
    fg=WHITE,
    font=("Arial", 10)
).pack(anchor="w")

password_entry = tk.Entry(
    login_frame,
    bg=BG,
    fg=WHITE,
    insertbackground=WHITE,
    font=("Arial", 11),
    show="*",
    bd=0
)
password_entry.pack(fill="x", pady=(7, 20), ipady=10)


# ------------------ LOGIN FUNCTION ------------------

def login():
    username = username_entry.get().strip()
    password = password_entry.get()

    if not username or not password:
        messagebox.showwarning(
            "Missing Information",
            "Please enter your username and password."
        )
        return

    if username == ADMIN_USERNAME and password == ADMIN_PASSWORD:

        dashboard_path = os.path.join(BASE_DIR, "dashboard.py")

        if not os.path.exists(dashboard_path):
            messagebox.showerror(
                "File Not Found",
                "dashboard.py could not be found."
            )
            return

        try:
            subprocess.Popen(
                [sys.executable, dashboard_path, "--authenticated"],
                cwd=BASE_DIR
            )
            root.destroy()

        except Exception as error:
            messagebox.showerror(
                "Error",
                f"Could not open dashboard:\n{error}"
            )

    else:
        messagebox.showerror(
            "Login Failed",
            "Incorrect username or password."
        )
        password_entry.delete(0, tk.END)


# ------------------ LOGIN BUTTON ------------------

tk.Button(
    login_frame,
    text="LOGIN",
    command=login,
    bg=GOLD,
    fg=BG,
    activebackground="#B8962E",
    activeforeground=BG,
    font=("Arial", 11, "bold"),
    bd=0,
    cursor="hand2"
).pack(fill="x", ipady=12, pady=10)

tk.Label(
    login_frame,
    text="Authorized Administrators Only",
    bg=CARD,
    fg=MUTED,
    font=("Arial", 8)
).pack(pady=10)

# Press Enter to log in
root.bind("<Return>", lambda event: login())

username_entry.focus()
root.mainloop()
