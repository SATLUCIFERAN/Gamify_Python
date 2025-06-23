
# powerup.py
import random

class PowerUp:
    def __init__(self, board, kind, pos, duration=5000):
        self.board    = board
        self.kind     = kind         # e.g. "widen"
        self.x, self.y= pos          # grid cell where it will fall
        self.cell     = board.cell_size
        self.id       = None
        self.duration = duration     # ms
        self.draw()

    def draw(self):
        if self.id: self.board.canvas.delete(self.id)
        px = self.x * self.cell + self.cell//2
        py = self.y * self.cell + self.cell//2
        color = "green" if self.kind=="widen" else "white"
        r = self.cell//2
        self.id = self.board.canvas.create_oval(px-r,py-r,px+r,py+r,fill=color)

    def fall(self):
        """Call each tick: move down one cell and redraw."""
        self.y += 1
        self.draw()
