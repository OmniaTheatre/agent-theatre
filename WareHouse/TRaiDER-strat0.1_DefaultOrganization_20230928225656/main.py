'''
Main file for the automated trading algorithm.
'''
import tkinter as tk
from tkinter import messagebox
from trading_algorithm import TradingAlgorithm
# Create the main application window
window = tk.Tk()
window.title("Automated Trading Algorithm")
# Create an instance of the TradingAlgorithm class
trading_algorithm = TradingAlgorithm()
# Define a function to handle the button click event
def run_algorithm():
    result = trading_algorithm.run()
    messagebox.showinfo("Algorithm Result", result)
# Create a button to run the algorithm
run_button = tk.Button(window, text="Run Algorithm", command=run_algorithm)
run_button.pack()
# Start the main event loop
tk.mainloop()