'''
Main file for the algorithmic trading application.
'''
import tkinter as tk
from gui import Application
if __name__ == "__main__":
    root = tk.Tk()
    app = Application(root)
    app.mainloop()