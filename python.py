import tkinter as tk
from tkinter import messagebox

def check_password():
    password = entry.get()

    has_number = any(char.isdigit() for char in password)
    has_symbol = any(not char.isalnum() for char in password)

    if len(password) <= 8:
        messagebox.showerror("Weak Password", "Password should be more than 8 characters")
    elif not has_number:
        messagebox.showerror("Weak Password", "Add at least 1 number")
    elif not has_symbol:
        messagebox.showerror("Weak Password", "Add at least 1 symbol")
    else:
        messagebox.showinfo("Success", "Password Successfully Generated ✅")

# Create the window
root = tk.Tk()
root.title("Password Checker")
root.geometry("350x200")

# Label
label = tk.Label(root, text="Enter your password:", font=("Arial", 12))
label.pack(pady=10)

# Entry box
entry = tk.Entry(root, show="*", font=("Arial", 12))
entry.pack(pady=5)

# Button
check_btn = tk.Button(root, text="Check Password", command=check_password, font=("Arial", 12))
check_btn.pack(pady=20)

# Run
root.mainloop()

