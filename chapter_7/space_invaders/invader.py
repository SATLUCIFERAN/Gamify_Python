
# invader.py
from bomb import Bomb

class Invader:
    """
    A single alien in the invader swarm.
    grid_x, grid_y : its position in the invisible grid
    cell_size      : pixels per grid cell (from Board)
    """
    def __init__(self, board, grid_x, grid_y, speed=1, color="green"):
        self.board    = board
        self.cell     = board.cell_size
        self.grid_x   = grid_x
        self.grid_y   = grid_y
        self.speed    = speed         # how many cells per tick
        self.direction = 1            # 1 = right, -1 = left
        self.id       = None          # canvas object id
        self.alive    = True
        self.color     = color
        self.draw()                    # paint on creation

    def draw(self):
        """Erase old and draw a square (or simple sprite) at current grid cell."""
        if self.id:
            self.board.canvas.delete(self.id)

        x1 = self.grid_x * self.cell
        y1 = self.grid_y * self.cell
        x2 = x1 + self.cell
        y2 = y1 + self.cell

        self.id = self.board.canvas.create_rectangle(
            x1, y1, x2, y2,
            fill=self.color, outline="black"
        )

    def move(self, grid_width):
        """
        Advance horizontally. If we hit the edge (0 or grid_width-1),
        reverse direction, drop down one row, then continue.
        """
        # compute next x
        nx = self.grid_x + self.direction * self.speed

        # edge check
        if nx < 0 or nx >= grid_width:
            self.direction *= -1           # reverse horizontal motion
            self.grid_y   += 1             # drop down
            nx = self.grid_x + self.direction * self.speed

        self.grid_x = nx
        self.draw()

    def hit(self):
        """Called when a bullet collides: mark dead and erase."""
        self.alive = False
        if self.id:
            self.board.canvas.delete(self.id)
            self.id = None


    def drop_bomb(self):
        """
        Create and return a Bomb just beneath this invader.
        """
        # drop from the cell directly below the invader
        return Bomb(self.board, self.grid_x, self.grid_y + 1, speed=1, color="red")