
# effects.py

import pygame

class SoundManager:
    """Load and play laser, explosion, and game-over sounds via pygame.mixer."""
    def __init__(self, laser_file, explosion_file, game_over_file=None):
        pygame.mixer.init()
        self.laser    = pygame.mixer.Sound(laser_file)
        self.explosion= pygame.mixer.Sound(explosion_file)
        self.game_over= pygame.mixer.Sound(game_over_file) if game_over_file else None

    def play_laser(self):
        self.laser.play()

    def play_explosion(self):
        self.explosion.play()

    def play_game_over(self):
        if self.game_over:
            self.game_over.play()


class Explosion:
 
    def __init__(self, board, x, y, max_r=20, steps=5, color="yellow"):
        self.canvas = board.canvas
        self.cell   = board.cell_size
        self.color  = color
        # Convert grid→pixel center
        px = x * self.cell + self.cell // 2
        py = y * self.cell + self.cell // 2
        self.px, self.py = px, py

        self.max_r = max_r
        self.steps = steps
        self.current = 0
        self.id = None
        self._animate()

    def _animate(self):
        """Draw one frame, then schedule the next."""
        # Remove previous circle
        if self.id:
            self.canvas.delete(self.id)

        # Compute radius for this frame
        frac = (self.current + 1) / self.steps
        r = int(self.max_r * frac)

        # Draw new circle
        self.id = self.canvas.create_oval(
            self.px - r, self.py - r,
            self.px + r, self.py + r,
            outline=self.color
        )

        self.current += 1
        if self.current < self.steps:
            # Schedule next frame in 50ms
            self.canvas.after(50, self._animate)
        else:
            # Final clean-up
            self.canvas.delete(self.id)
