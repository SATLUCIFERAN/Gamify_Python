# snake.py

class Snake:
    """
    Represents the snake in the game as a list of (x,y) segments.
    """
    def __init__(self, start_pos, start_length=3, direction=(1, 0)):
        """
        Initialize the snake centered at start_pos, with a given length
        and initial movement direction.
        """
        self.direction = direction             # Current movement vector
        x, y = start_pos
        # Build initial segments: head at front, tail extending backward
        self.segments = [
            (x - i*direction[0], y - i*direction[1])
            for i in range(start_length)
        ]
        self.growing = False                   # Flag to grow on next move

    def change_direction(self, new_direction):
        """
        Update direction unless new_direction is directly opposite
        (to prevent immediate 180° turns).
        """
        dx, dy = self.direction
        ndx, ndy = new_direction
        # Disallow reversing
        if (dx + ndx, dy + ndy) != (0, 0):
            self.direction = new_direction

    def move(self):
        """
        Advance the snake by one unit in the current direction.
        If self.growing is False, remove the tail; otherwise keep it.
        """
        head_x, head_y = self.segments[0]
        dx, dy = self.direction
        new_head = (head_x + dx, head_y + dy)

        # Insert new head at front
        self.segments.insert(0, new_head)

        # Remove tail unless growing
        if self.growing:
            self.growing = False   # Reset flag
        else:
            self.segments.pop()    # Drop the last segment

    def grow(self):
        """
        Signal that on the next move, the snake should grow
        (i.e., skip tail removal).
        """
        self.growing = True

    def collides_with_self(self):
        """
        Return True if the head shares a position with any other segment.
        """
        head = self.segments[0]
        return head in self.segments[1:]
