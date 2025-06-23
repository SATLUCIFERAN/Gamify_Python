# board.py
import tkinter as tk

class Board:
    def __init__(self, master, grid_width, grid_height, cell_size=20):
        """
        master: the tk.Tk() root
        grid_width, grid_height: number of cells horizontally and vertically
        cell_size: pixel size of each cell
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.cell_size = cell_size

        # Calculate canvas pixel dimensions
        canvas_w = grid_width * cell_size
        canvas_h = grid_height * cell_size

        # 1) Create the Canvas widget
        self.canvas = tk.Canvas(master, width=canvas_w, height=canvas_h + 30)
        self.canvas.pack()

        # 2) Score label below the canvas
        self.score_text = self.canvas.create_text(
            5, canvas_h + 15,
            anchor="w", text="Score: 0", font=("Arial", 12)
        )

    def clear(self):
        """Remove all drawn items except the score text."""
        self.canvas.delete("snake")
        self.canvas.delete("food")

    def draw_snake(self, segments):
        """
        Draw each segment as a green rectangle.
        segments: list of (x, y) tuples.
        """
        for x, y in segments:
            x1 = x * self.cell_size
            y1 = y * self.cell_size
            x2 = x1 + self.cell_size
            y2 = y1 + self.cell_size
            # Tag each piece as "snake" so we can clear them easily
            self.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill="green", outline="black",
                tags="snake"
            )

    def draw_food(self, position):
        """
        Draw the food as a red oval.
        position: (x, y) tuple.
        """
        x, y = position
        x1 = x * self.cell_size
        y1 = y * self.cell_size
        x2 = x1 + self.cell_size
        y2 = y1 + self.cell_size
        self.canvas.create_oval(
            x1, y1, x2, y2,
            fill="red", tags="food"
        )

    def update_score(self, score):
        """Change the score label text."""
        self.canvas.itemconfigure(self.score_text, text=f"Score: {score}")



