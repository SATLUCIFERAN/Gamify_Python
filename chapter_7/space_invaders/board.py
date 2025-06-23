# board.py

import tkinter as tk

class Board:
    def __init__(self, master, grid_width, grid_height, cell_size):
        self.grid_width  = grid_width
        self.grid_height = grid_height
        self.cell_size   = cell_size

        # Create a Canvas widget sized in pixels
        self.canvas = tk.Canvas(
            master,
            width  = grid_width  * cell_size,
            height = grid_height * cell_size,
            bg="black"
        )
        self.canvas.pack()

        # Initialize the score/lives display string
        self._score_display = "Score: 0    Lives: 0"

        # Draw score & lives text at top-left and keep its ID
        self.score_text = self.canvas.create_text(
            10, 10,
            anchor="nw",
            fill="white",
            font=("Arial", 14),
            text=self._score_display
        )

    def clear(self):
        """Erase all shapes except the score text."""
        # Delete everything on the canvas…
        self.canvas.delete("all")
        # …then redraw the latest score & lives text
        self.score_text = self.canvas.create_text(
            10, 10,
            anchor="nw",
            fill="white",
            font=("Arial", 14),
            text=self._score_display
        )

    def update_score(self, score, lives):
        """Update the on-screen score & lives display."""
        # Update the backing string
        self._score_display = f"Score: {score}    Lives: {lives}"
        # Change the existing text object in-place
        self.canvas.itemconfigure(
            self.score_text,
            text=self._score_display
        )
