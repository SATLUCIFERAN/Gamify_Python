
# utils.py
import pygame
from my_snake.board import WHITE

def draw_grid(surface):
    """
    Optional: draw grid lines for reference.
    """
    width, height = surface.get_size()
    block = pygame.display.get_surface().get_width() // (width // block)
    # implement if desired


def draw_text(surface, text, size, x, y):
    """
    Render text at (x, y) on the surface.
    """
    font = pygame.font.SysFont(None, size)
    text_surface = font.render(text, True, WHITE)
    surface.blit(text_surface, (x, y))