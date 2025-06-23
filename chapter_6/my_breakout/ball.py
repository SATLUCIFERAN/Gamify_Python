# ball.py
import random

class Ball:
    def __init__(self, board, start_pos=(5,10), speed_cells=1, 
                 dir_x=None, dir_y=-1, color="white"):
        """
        board: the Board instance (knows grid size & cell_size)
        start_pos: (x,y) in grid cells for initial ball location
        speed_cells: number of cells to move each tick (usually 1)
        dir_x, dir_y: initial direction vector; if None, randomize dir_x
        """
        self.board = board
        self.cell = board.cell_size
        self.grid_w, self.grid_h = board.grid_width, board.grid_height

        # 1) Position in grid coords and speed
        self.x, self.y = start_pos
        self.speed = speed_cells

        # 2) Direction vector (dx,dy), normalized so |dx| + |dy| = 1
        if dir_x is None:
            dir_x = random.choice([-1, 1])
        self.dx, self.dy = dir_x, dir_y

        # 3) Canvas ID for drawing
        self.id = None
        self.color = color
        self.draw()

    def draw(self):
        """Erase old and draw the ball as a circle at its current (x,y)."""
        if self.id:
            self.board.canvas.delete(self.id)
        px = self.x * self.cell + self.cell // 2
        py = self.y * self.cell + self.cell // 2
        r  = self.cell // 2
        self.id = self.board.canvas.create_oval(
            px - r, py - r, px + r, py + r,
            fill=self.color, tags="ball"
        )

    def move(self):
        """Compute new position, handle wall bounces, then redraw."""
        # a) Advance
        new_x = self.x + self.dx * self.speed
        new_y = self.y + self.dy * self.speed

        # b) Left/Right wall bounce
        if new_x < 0 or new_x >= self.grid_w:
            self.dx *= -1
            new_x = self.x + self.dx * self.speed  # recalc

        # c) Top wall bounce
        if new_y < 0:
            self.dy *= -1
            new_y = self.y + self.dy * self.speed

        # d) Update coords
        self.x, self.y = new_x, new_y

        # e) Redraw
        self.draw()

    def bounce_vertical(self):
        """Reverse vertical direction (e.g., paddle or brick bounce)."""
        self.dy *= -1

    def bounce_horizontal(self):
        """Reverse horizontal direction (e.g., side of a brick)."""
        self.dx *= -1
