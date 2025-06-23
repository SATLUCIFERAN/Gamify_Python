
import pygame
from settings import ENEMY_SPEED, ENEMY_COLOR

class Enemy:
    def __init__(self, x, y, patrol_area):
        """
        Initialize an enemy at (x, y) that moves horizontally within patrol_area tuple (x_min, x_max).
        """
        self.rect = pygame.Rect(x, y, 32, 32)  # 32×32 px square
        self.speed = ENEMY_SPEED
        self.patrol_area = patrol_area
        self.direction = 1  # 1 = right, -1 = left

    def update(self):
        """
        Move enemy within patrol bounds and reverse direction at edges.
        """
        self.rect.x += self.speed * self.direction
        if self.rect.x < self.patrol_area[0] or self.rect.x > self.patrol_area[1]:
            self.direction *= -1
            # Flip position back inside bounds
            self.rect.x = max(self.patrol_area[0], min(self.rect.x, self.patrol_area[1]))

    def draw(self, screen):
        """
        Draw the enemy as a rectangle or sprite.
        """
        # If using a placeholder color:
        pygame.draw.rect(screen, ENEMY_COLOR, self.rect)
        # To use a sprite: replace above with screen.blit(enemy_image, self.rect)