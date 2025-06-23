# player.py

from bullet import Bullet

class Player:
    def __init__(self, board, lives=3, speed=1, color="white"):
        """
        board:   Board instance (knows canvas, grid_size, cell_size)
        lives:   number of hits the player can take
        speed:   how many cells to move per key press
        color:   fill color of the ship
        """
        # Store references & constants
        self.board      = board
        self.cell       = board.cell_size
        self.grid_w     = board.grid_width
        self.grid_h     = board.grid_height
        self.lives      = lives
        self.alive      = True
        self.speed      = speed
        self.color      = color

        # Starting position: centered on bottom row
        self.x          = self.grid_w // 2
        self.y          = self.grid_h - 1

        # Projectiles fired by the player
        self.bullets    = []

        # Canvas ID for erasing/redrawing
        self.id         = None

        # Draw the ship immediately
        self.draw()

    def move(self, dx):
        """
        Move the ship left or right by dx * speed cells,
        clamped to the playfield.
        """
        new_x = self.x + dx * self.speed
        self.x = max(0, min(new_x, self.grid_w - 1))
        self.draw()

    def fire(self):
        """
        Create a Bullet just above the ship, traveling up,
        add it to our bullets list, and return it so the
        main loop can track and draw it.
        """
        b = Bullet(
            board   = self.board,
            start_x = self.x,
            start_y = self.y - 1,
            speed   = 1,              # cells per tick upward
            color   = self.color
        )
        self.bullets.append(b)
        return b

    def draw(self):
        """
        Erase the old ship (if any) and draw a new
        triangular polygon centered in cell (self.x, self.y).
        """
        if self.id:
            self.board.canvas.delete(self.id)

        px = self.x * self.cell + self.cell // 2
        py = self.y * self.cell + self.cell // 2
        r  = self.cell // 2
        points = [
            px - r, py + r,   # bottom-left
            px    , py - r,   # top (nose)
            px + r, py + r    # bottom-right
        ]
        self.id = self.board.canvas.create_polygon(
            points, fill=self.color, outline="black"
        )

    def update_bullets(self):
        """
        Move each bullet in self.bullets, and remove any
        that have gone ‘dead’ (off screen or on collision).
        """
        for b in list(self.bullets):
            b.move()
            if not b.alive:
                self.bullets.remove(b)

    def contains(self, x, y):
        """
        Return True if the ship currently occupies grid cell (x,y).
        """
        return self.alive and x == self.x and y == self.y

    def hit(self):
        """
        Called when an invader bomb strikes us:
        lose one life, and if you’re out of lives mark dead and erase.
        """
        if not self.alive:
            return

        self.lives -= 1
        if self.lives <= 0:
            self.alive = False
            if self.id:
                self.board.canvas.delete(self.id)
