import tkinter as tk
from math import *

class ScientificCalculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Scientific Calculator")
        self.expression = ''
        self.result_var = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        self.result_entry = tk.Entry(self.root, textvariable=self.result_var, font=('Arial', 20), bd=5, insertwidth=4, width=20, justify='right')
        self.result_entry.grid(row=0, column=0, columnspan=6, padx=10, pady=10)

        buttons = [
            'C', '(', ')', 'sqrt',
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+',
            'sin', 'cos', 'tan', 'log'
        ]

        button_row = 1
        button_col = 0
        for button_text in buttons:
            button = tk.Button(self.root, text=button_text, padx=20, pady=20, font=('Arial', 14), command=lambda btn=button_text: self.on_button_click(btn))
            button.grid(row=button_row, column=button_col, padx=5, pady=5, sticky='nsew')

            if button_text in ['C', 'sin', 'cos', 'tan', 'log', 'sqrt']:
                button.config(bg='lightblue', fg='black')
            elif button_text == '=':
                button.config(bg='orange', fg='white')
            else:
                button.config(bg='lightgreen', fg='black')

            button_col += 1
            if button_col > 3:
                button_col = 0
                button_row += 1

    def on_button_click(self, button_text):
        if button_text == '=':
            try:
                self.expression = str(eval(self.expression))
            except Exception as e:
                self.expression = 'Error'
            self.result_var.set(self.expression)
        elif button_text == 'C':
            self.expression = ''
            self.result_var.set('')
        elif button_text in ['sin', 'cos', 'tan', 'log', 'sqrt']:
            self.expression += button_text + '('
            self.result_var.set(self.expression)
        else:
            self.expression += button_text
            self.result_var.set(self.expression)

if __name__ == "__main__":
    root = tk.Tk()
    app = ScientificCalculator(root)
    root.mainloop()
