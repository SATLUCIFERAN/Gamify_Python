# brick.py
import tkinter as tk

class Brick:
    COLORS = {1: "red", 2: "orange", 3: "yellow"}  

    def __init__(self, board, grid_x, grid_y, hits=1):
       
        self.board  = board
        self.cell   = board.cell_size
        self.grid_x = grid_x
        self.grid_y = grid_y
        self.hits   = hits
        self.id     = None
        self.draw()

    def draw(self):
        """Erase old and draw a rectangle colored by remaining hits."""
        # 0) Remove prior rectangle
        if self.id:
            self.board.canvas.delete(self.id)

        # 1) Compute pixel corners of the brick
        x1 = self.grid_x * self.cell
        y1 = self.grid_y * self.cell
        x2 = x1 + self.cell
        y2 = y1 + self.cell

        # 2) Choose color based on hits (default to gray)
        color = Brick.COLORS.get(self.hits, "gray")

        # 3) Draw a filled rectangle and save its ID
        self.id = self.board.canvas.create_rectangle(
            x1, y1, x2, y2, fill=color, outline="black"
        )

    def contains_cell(self, x, y):
      
        return (x == self.grid_x) and (y == self.grid_y)

    def hit(self):
        """
        Called when the ball strikes this brick.
        Decrement hits, redraw (or delete if gone).
        """
        self.hits -= 1
        if self.hits <= 0:
            # Remove from canvas
            if self.id:
                self.board.canvas.delete(self.id)
                self.id = None
        else:
            # Just redraw with updated color
            self.draw()
