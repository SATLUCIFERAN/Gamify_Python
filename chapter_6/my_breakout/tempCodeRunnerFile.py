import os
import tkinter as tk
import pygame
from board import Board
from paddle import Paddle
from ball import Ball
from brick import Brick
from levels import load_level

class SoundManager:
    """Simple wrapper around pygame.mixer.Sound for game audio."""
    def __init__(self, bounce_file, brick_file, game_over_file=None):
        pygame.mixer.init()
        self.snd_bounce    = pygame.mixer.Sound(bounce_file)
        self.snd_brick     = pygame.mixer.Sound(brick_file)
        self.snd_game_over = pygame.mixer.Sound(game_over_file) if game_over_file else None

    def play_bounce(self):
        self.snd_bounce.play()

    def play_brick(self):
        self.snd_brick.play()

    def play_game_over(self):
        if self.snd_game_over:
            self.snd_game_over.play()

class Breakout:
    def __init__(
        self,
        level_file="level1.json",
        grid_w=20,
        grid_h=30,
        cell_size=20,
        fps=30
    ):
        # Determine base directory for assets
        base_dir = os.path.dirname(os.path.abspath(__file__))

        # Initialize Pygame (audio) and Tkinter (GUI)
        pygame.init()
        self.master = tk.Tk()
        self.master.title("Breakout")
        self.board = Board(self.master, grid_w, grid_h, cell_size)

        # Paddle & Ball
        self.paddle = Paddle(self.board, width_cells=5, color="blue")
        self.ball = Ball(
            self.board,
            start_pos=(grid_w // 2, grid_h - 6),
            speed_cells=1
        )

        # Load brick layout from JSON within levels directory
        level_path = os.path.join(base_dir, "levels", level_file)
        level_data = load_level(level_path)
        layout = level_data.get("layout", [])
        self.bricks = [
            Brick(self.board, x, y, hits)
            for y, row in enumerate(layout)
            for x, hits in enumerate(row)
            if isinstance(hits, int) and hits > 0
        ]

        # Score, Lives & Sound
        self.score = 0
        self.lives = 3
        sounds_dir = os.path.join(base_dir, "sounds")
        self.snd = SoundManager(
            bounce_file=os.path.join(sounds_dir, "bounce.wav"),
            brick_file=os.path.join(sounds_dir, "brick.wav"),
            game_over_file=os.path.join(sounds_dir, "game_over.wav")
        )

        # Bind keys and start game loop
        self.master.bind("<Left>", lambda e: self.paddle.move(-1))
        self.master.bind("<Right>", lambda e: self.paddle.move(1))
        self.delay = int(1000 / fps)
        self.tick()
        self.master.mainloop()

    def tick(self):
        # Move ball and handle collisions
        self.ball.move()
        bx, by = self.ball.x, self.ball.y

        # Ball falls off bottom
        if by >= self.board.grid_height:
            self.lives -= 1
            self.snd.play_bounce()
            if self.lives == 0:
                self.snd.play_game_over()
                return self.game_over()
            # Reset positions
            self.ball.x, self.ball.y = (self.board.grid_width//2, self.board.grid_height-6)
            self.ball.dx, self.ball.dy = (1, -1)
            self.paddle.x = (self.board.grid_width - self.paddle.width_cells)//2

        # Wall collisions
        if bx in (0, self.board.grid_width-1) or by == 0:
            self.snd.play_bounce()

        # Paddle collision
        px, py, pw = (self.paddle.x, self.paddle.y, self.paddle.width_cells)
        if by == py - 1 and px <= bx < px + pw:
            self.ball.bounce_vertical()
            self.snd.play_bounce()
            self.score += 1

        # Brick collisions
        for brick in list(self.bricks):
            if brick.contains_cell(bx, by):
                brick.hit()
                self.ball.bounce_vertical()
                self.snd.play_brick()
                if brick.hits == 0:
                    self.bricks.remove(brick)
                    self.score += 10
                break

        # Redraw board
        self.board.clear()
        for brick in self.bricks:
            brick.draw()
        self.paddle.draw()
        self.ball.draw()
        self.board.update_score(self.score, self.lives)

        # Schedule next frame
        self.master.after(self.delay, self.tick)

    def game_over(self):
        # Display GAME OVER
        cx = (self.board.grid_width * self.board.cell_size)//2
        cy = (self.board.grid_height * self.board.cell_size)//2
        self.board.canvas.create_text(
            cx, cy,
            text="GAME OVER",
            fill="red",
            font=("Arial", 32)
        )

if __name__ == "__main__":
    Breakout()
