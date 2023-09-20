'''
This file contains the Calculator class that represents the calculator application.
'''
import tkinter as tk
import numexpr as ne
import sys
class Calculator:
    def __init__(self, root):
        self.root = root
        self.root.title("Calculator")
        self.entry = tk.Entry(self.root, width=30)
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)
        self.create_buttons()
    def create_buttons(self):
        buttons = [
            '7', '8', '9', '/',
            '4', '5', '6', '*',
            '1', '2', '3', '-',
            '0', '.', '=', '+'
        ]
        row = 1
        col = 0
        for button in buttons:
            tk.Button(self.root, text=button, width=7, height=3, command=lambda btn=button: self.button_click(btn)).grid(row=row, column=col, padx=5, pady=5)
            col += 1
            if col > 3:
                col = 0
                row += 1
    def button_click(self, value):
        current_value = self.entry.get()
        if value == '=':
            try:
                if '/ 0' in current_value:
                    raise ZeroDivisionError("Division by zero")
                result = ne.evaluate(current_value)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, str(result))
            except Exception as e:
                error_message = str(e)
                print("Error:", error_message)
                self.entry.delete(0, tk.END)
                self.entry.insert(tk.END, error_message)
        else:
            self.entry.insert(tk.END, value)