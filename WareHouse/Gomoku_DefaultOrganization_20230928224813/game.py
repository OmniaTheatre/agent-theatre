'''
This is the game module for the Gomoku game.
'''
import tkinter as tk
class Game:
    def __init__(self, root):
        self.root = root
        self.board = [[0] * 15 for _ in range(15)]  # 15x15 game board
        self.current_player = 1  # Player 1 starts the game
        self.game_over = False
        self.canvas = tk.Canvas(self.root, width=450, height=450, bg="white")
        self.canvas.pack()
        self.canvas.bind("<Button-1>", self.on_click)
    def start(self):
        '''
        Starts the game by drawing the game board.
        '''
        self.draw_board()
    def draw_board(self):
        '''
        Draws the game board on the canvas.
        '''
        self.canvas.delete("all")
        for i in range(15):
            self.canvas.create_line(i * 30, 0, i * 30, 450)
            self.canvas.create_line(0, i * 30, 450, i * 30)
    def on_click(self, event):
        '''
        Handles the click event on the canvas.
        '''
        if self.game_over:
            return
        x = event.x // 30
        y = event.y // 30
        if self.board[y][x] == 0:
            self.board[y][x] = self.current_player
            self.draw_piece(x, y, self.current_player)
            if self.check_win(x, y):
                self.game_over = True
                self.show_winner()
            self.current_player = 3 - self.current_player  # Switch player
    def draw_piece(self, x, y, player):
        '''
        Draws a game piece on the canvas.
        '''
        color = "black" if player == 1 else "white"
        self.canvas.create_oval(x * 30 + 5, y * 30 + 5, x * 30 + 25, y * 30 + 25, fill=color)
    def check_win(self, x, y):
        '''
        Checks if a player has won the game.
        '''
        directions = [(1, 0), (0, 1), (1, 1), (1, -1)]  # Check in horizontal, vertical, and diagonal directions
        for dx, dy in directions:
            count = 1
            count += self.count_pieces(x, y, dx, dy)
            count += self.count_pieces(x, y, -dx, -dy)
            if count >= 5:
                return True
        return False
    def count_pieces(self, x, y, dx, dy):
        '''
        Counts the number of consecutive pieces in a given direction.
        '''
        player = self.board[y][x]
        count = 0
        while True:
            x += dx
            y += dy
            if x < 0 or y < 0 or x >= 15 or y >= 15 or self.board[y][x] != player:
                break
            count += 1
        return count - 1  # Subtract 1 to exclude the starting piece
    def show_winner(self):
        '''
        Displays the winner of the game on the canvas.
        '''
        winner = "Player 1" if self.current_player == 2 else "Player 2"
        self.canvas.create_text(225, 225, text=f"{winner} wins!", font=("Arial", 20), fill="red")