
# barrier.py

class Barrier:
    """
    A destructible bunker made of individual cells.
    Each cell lives at a grid (x,y) and can take one hit.
    """
    # A simple 3×2 block shape, relative coords
    SHAPE = [
        (0,0),(1,0),(2,0),
        (0,1),(1,1),(2,1)
    ]

    def __init__(self, board, origin_x, origin_y, strength=1, color="gray"):
        """
        board      : Board instance (canvas + cell_size)
        origin_x/y : top-left grid cell for this barrier
        color      : fill color of intact segments
        """
        self.board   = board
        self.cell    = board.cell_size
        self.color   = color

        # Build a set of live segment coordinates
        self.segments = {
            (origin_x + dx, origin_y + dy)
            for dx,dy in Barrier.SHAPE
        }
        # Map each segment to its canvas ID for easy deletion
        self._ids = {}

        # Draw initial bunker
        self.draw()

    def draw(self):
        """Erase all old segments, then draw each remaining one."""
        # 0) Remove every prior rectangle
        for cid in self._ids.values():
            self.board.canvas.delete(cid)
        self._ids.clear()

        # 1) For each live segment, compute pixel corners and draw
        for (gx, gy) in self.segments:
            x1 = gx * self.cell
            y1 = gy * self.cell
            x2 = x1 + self.cell
            y2 = y1 + self.cell
            cid = self.board.canvas.create_rectangle(
                x1, y1, x2, y2,
                fill=self.color, outline="black"
            )
            self._ids[(gx, gy)] = cid

    def contains(self, x, y):
        """
        Return True if a bullet or bomb at grid (x,y)
        would strike this bunker.
        """
        return (x, y) in self.segments

    def hit(self, x, y):
        """
        Called when a projectile strikes grid (x,y).
        If that segment exists, remove it and erase its drawing.
        """
        if (x, y) not in self.segments:
            return False  # nothing was hit here

        # 1) Remove the segment from logic
        self.segments.remove((x, y))
        # 2) Delete its rectangle from the canvas
        cid = self._ids.pop((x, y), None)
        if cid:
            self.board.canvas.delete(cid)
        return True
