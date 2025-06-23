
# bullet.py

class Bullet:
    """
    A single shot fired by the player.
    - board:      Board instance (canvas + cell_size)
    - x, y:       integer grid coordinates of the bullet's *tip*
    - speed:      how many cells upward per tick
    - alive:      whether it's still on-screen
    """
    def __init__(self, board, start_x, start_y, speed=1, color="white"):
        self.board  = board
        self.cell   = board.cell_size
        self.x      = start_x      # column of bullet tip
        self.y      = start_y      # row of bullet tip
        self.speed  = speed
        self.color  = color
        self.id     = None
        self.alive  = True
        self.draw()

    def draw(self):
        """Erase old shape, then draw a 1×2-pixel-tall line centered in the cell."""
        # 1) Remove previous
        if self.id is not None:
            self.board.canvas.delete(self.id)

        if not self.alive:
            return

        # 2) Compute pixel coordinates
        px = self.x * self.cell + self.cell // 2
        py = self.y * self.cell

        # 3) Draw a small vertical line or rectangle
        half = self.cell // 8  # make it narrow
        self.id = self.board.canvas.create_rectangle(
            px - half, py,
            px + half, py + self.cell // 4,
            fill=self.color
        )

    def move(self):
        """Advance upward; if off top, mark dead and erase."""
        if not self.alive:
            return

        self.y -= self.speed   # go up by speed cells

        # Off the top?
        if self.y < 0:
            self.alive = False
            if self.id is not None:
                self.board.canvas.delete(self.id)
                self.id = None
            return

        # Otherwise, redraw at new position
        self.draw()

    def hit(self):
        """Called when colliding with an invader: die immediately."""
        if not self.alive:
            return
        self.alive = False
        if self.id is not None:
            self.board.canvas.delete(self.id)
            self.id = None
