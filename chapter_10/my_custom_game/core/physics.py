
import pygame
from settings import GRAVITY

def apply_gravity(rect, vel_y, platforms):
    """
    Update vel_y and rect.y by gravity, then resolve collisions with platforms.
    Returns updated vel_y.
    """
    # 1. Apply gravity
    vel_y += GRAVITY
    rect.y += vel_y

    # 2. Check collisions
    for p in platforms:
        if rect.colliderect(p):
            # Landing on top of platform
            if vel_y > 0 and rect.bottom >= p.top:
                rect.bottom = p.top
                vel_y = 0
            # Hitting head on platform
            elif vel_y < 0 and rect.top <= p.bottom:
                rect.top = p.bottom
                vel_y = 0
            break
    return vel_y

# Example usage in Player.update:
# self.vel_y = apply_gravity(self.rect, self.vel_y, platforms)