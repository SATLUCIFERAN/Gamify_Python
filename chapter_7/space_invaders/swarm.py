
# swarm.py

from invader import Invader
import random

class Swarm:
    """
    Manages a formation of Invader objects:
      - rows, cols: number of aliens per row/column
      - h_spacing, v_spacing: empty cells between invaders
      - speed: how fast they march (cells per tick)
    """
    def __init__(self, board, rows, cols,
                 h_spacing=1, v_spacing=1,
                 speed=1, color="green"):
        self.board     = board
        self.rows      = rows
        self.cols      = cols
        self.h_spacing = h_spacing
        self.v_spacing = v_spacing
        self.speed     = speed
        self.invaders  = []

        # Instantiate one Invader per grid slot:
        for r in range(rows):
            for c in range(cols):
                gx = c * (1 + h_spacing)
                gy = r * (1 + v_spacing)
                alien = Invader(
                    board,
                    grid_x=gx, grid_y=gy,
                    speed=speed,
                    color=color
                )
                self.invaders.append(alien)

    def move(self,grid_width):
        """
        Advance the entire formation:
        1. Check if any alive invader would go off-screen next tick.
        2. If so: reverse direction for all, and drop every row by +1.
        3. Otherwise: simply advance each alive invader horizontally.
        """
        gw = self.board.grid_width
        # 1) Would any alien hit the left/right edge?
        edge_hit = False
        for inv in self.invaders:
            if inv.alive:
                nx = inv.grid_x + inv.direction * inv.speed
                if nx < 0 or nx >= gw:
                    edge_hit = True
                    break

        # 2) If we hit the edge, drop & reverse, else just march forward
        if edge_hit:
            for inv in self.invaders:
                if inv.alive:
                    inv.grid_y += 1             # drop down one row
                    inv.direction *= -1         # reverse horizontal direction
                    inv.draw()
        else:
            for inv in self.invaders:
                if inv.alive:
                    inv.grid_x += inv.direction * inv.speed
                    inv.draw()

    def any_reached_bottom(self):
        """
        Returns True if any alive invader has reached the bottom row,
        signaling the player's defeat.
        """
        h = self.board.grid_height
        return any(
            inv.alive and inv.grid_y >= h - 1
            for inv in self.invaders
        )

    def all_dead(self):
        """
        Returns True when every invader has been shot,
        signaling the player's victory.
        """
        return not any(inv.alive for inv in self.invaders)


    def draw(self):
        """
        Draw every alive Invader in the swarm.
        Called once per frame after move().
        """
        for inv in self.invaders:
            if inv.alive:
                inv.draw()


    def random_invader(self):
        """Return a random alive Invader, or None if they're all dead."""
        alive = [inv for inv in self.invaders if inv.alive]
        return random.choice(alive) if alive else None

    def hit_invader_at(self, x, y):
        """
        Called when a player bullet is at (x,y).
        If there's an alive Invader there, kill it and return True.
        """
        for inv in self.invaders:
            if inv.alive and inv.grid_x == x and inv.grid_y == y:
                inv.hit()
                return True
        return False