# paddle.py
import tkinter as tk

class Paddle:
    def __init__(self, board, width_cells=4, color="blue"):
        """
        board: the Board instance (knows grid and cell_size)
        width_cells: how many grid cells wide the paddle is
        color: fill color for drawing
        """
        self.board = board
        self.width_cells = width_cells
        self.color = color

        # 1) Starting position: centered horizontally, one cell above bottom
        gw, gh = board.grid_width, board.grid_height
        self.y = gh - 1
        # x = leftmost cell; center paddle → (gw - width_cells)//2
        self.x = (gw - width_cells) // 2

        # 2) Draw initial paddle
        self.id = None
        self.draw()

    def draw(self):
        """Draws or redraws the paddle rectangle on the canvas."""
        # If already drawn, remove the old one
        if self.id:
            self.board.canvas.delete(self.id)

        cell = self.board.cell_size
        x1 = self.x * cell
        y1 = self.y * cell
        x2 = x1 + self.width_cells * cell
        y2 = y1 + cell

        # Draw a rectangle and keep its canvas ID
        self.id = self.board.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=self.color, tags="paddle"
        )

    def move(self, delta_cells):
        """
        Move the paddle left (delta_cells<0) or right (>0).
        Ensures it stays within [0, grid_width - width_cells].
        """
        new_x = self.x + delta_cells
        # 3) Enforce boundary limits
        max_left = 0
        max_right = self.board.grid_width - self.width_cells
        self.x = max(max_left, min(new_x, max_right))
        # 4) Redraw at its new position
        self.draw()
