
class Bomb:
    """
    A single bomb dropped by an invader.
    Behaves like a Bullet but moves DOWN the screen.
    """
    def __init__(self, board, start_x, start_y, speed=1, color="red"):
        self.board  = board
        self.cell   = board.cell_size
        self.x      = start_x
        self.y      = start_y
        self.speed  = speed
        self.color  = color
        self.id     = None
        self.alive  = True
        self.draw()

    def draw(self):
        if self.id is not None:
            self.board.canvas.delete(self.id)
        if not self.alive:
            return
        px = self.x * self.cell + self.cell // 2
        py = self.y * self.cell
        half = self.cell // 8
        self.id = self.board.canvas.create_rectangle(
            px - half, py,
            px + half, py + self.cell // 4,
            fill=self.color
        )

    def move(self):
        if not self.alive:
            return
        self.y += self.speed
        if self.y >= self.board.grid_height:
            self.alive = False
            if self.id:
                self.board.canvas.delete(self.id)
            return
        self.draw()

    def hit(self):
        """Called when the bomb strikes something."""
        if not self.alive:
            return
        self.alive = False
        if self.id:
            self.board.canvas.delete(self.id)