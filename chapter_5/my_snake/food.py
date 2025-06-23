# food.py
import random

class Food:
    """
    Represents the food pellet that the snake will eat.
    """
    def __init__(self, grid_width, grid_height, snake_segments):
        """
        Initialize by placing food somewhere not occupied by the snake.
        """
        self.grid_width = grid_width
        self.grid_height = grid_height
        self.position = self._random_position(snake_segments)

    def _random_position(self, snake_segments):
        """
        Return a random (x,y) within the grid that is not in snake_segments.
        """
        while True:
            x = random.randrange(self.grid_width)
            y = random.randrange(self.grid_height)
            if (x, y) not in snake_segments:
                return (x, y)

    def respawn(self, snake_segments):
        """
        Choose a new position after the snake has eaten the current food.
        """
        self.position = self._random_position(snake_segments)
