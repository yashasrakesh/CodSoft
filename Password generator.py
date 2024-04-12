import random
import string
import tkinter as tk
from tkinter import ttk

def generate_password(length, use_uppercase, use_digits, use_special_chars):
    chars = string.ascii_lowercase
    if use_uppercase:
        chars += string.ascii_uppercase
    if use_digits:
        chars += string.digits
    if use_special_chars:
        chars += string.punctuation

    password = ''.join(random.choice(chars) for _ in range(length))
    return password

def generate_password_gui():
    def generate():
        length = int(length_entry.get())
        use_uppercase = uppercase_var.get()
        use_digits = digits_var.get()
        use_special_chars = special_chars_var.get()

        password = generate_password(length, use_uppercase, use_digits, use_special_chars)
        password_var.set(password)

    root = tk.Tk()
    root.title("Password Generator")

    length_label = ttk.Label(root, text="Enter password length:")
    length_label.pack(pady=10)

    length_entry = ttk.Entry(root)
    length_entry.pack()

    uppercase_var = tk.BooleanVar()
    uppercase_check = ttk.Checkbutton(root, text="Include uppercase letters", variable=uppercase_var)
    uppercase_check.pack()

    digits_var = tk.BooleanVar()
    digits_check = ttk.Checkbutton(root, text="Include digits", variable=digits_var)
    digits_check.pack()

    special_chars_var = tk.BooleanVar()
    special_chars_check = ttk.Checkbutton(root, text="Include special characters", variable=special_chars_var)
    special_chars_check.pack()

    generate_button = ttk.Button(root, text="Generate Password", command=generate)
    generate_button.pack(pady=20)

    password_var = tk.StringVar()
    password_label = ttk.Label(root, text="Generated Password:")
    password_label.pack()

    password_display = ttk.Label(root, textvariable=password_var, font=("Courier", 20))
    password_display.pack(pady=10)

    root.mainloop()

generate_password_gui()
