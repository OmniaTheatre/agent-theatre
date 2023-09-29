'''
This is the main file for the Gomoku game.
'''
import tkinter as tk
from game import Game
def main():
    root = tk.Tk()
    root.title("Gomoku")
    game = Game(root)
    game.start()
    root.mainloop()
if __name__ == "__main__":
    main()