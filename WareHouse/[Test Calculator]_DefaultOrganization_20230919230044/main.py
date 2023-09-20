'''
This is the main file that runs the calculator application.
'''
import tkinter as tk
from calculator import Calculator
def main():
    root = tk.Tk()
    calculator = Calculator(root)
    root.mainloop()
if __name__ == "__main__":
    main()