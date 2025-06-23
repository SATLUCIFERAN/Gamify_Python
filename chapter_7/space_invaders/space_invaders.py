import os
import tkinter as tk
import pygame
import random

from board     import Board
from player    import Player
from invader   import Invader
from swarm     import Swarm
from barrier   import Barrier
from effects   import SoundManager, Explosion

class SpaceInvaders:
    def __init__(self,
                 grid_w=20, grid_h=25, cell=20,
                 rows=4, cols=8,
                 barrier_specs=[(4,20),(10,20),(16,20)],
                 fps=30):
        
        base = os.path.dirname(__file__)
        pygame.init()
        self.master = tk.Tk()
        self.master.title("Space Invaders")
        self.board = Board(self.master, grid_w, grid_h, cell)

        # ———— Game stats
        self.score = 0

        # ———— Player
        self.player = Player(self.board, color="cyan")

        # Initialize HUD
        self.board.update_score(self.score, self.player.lives)

        # ———— Invader Swarm
        self.swarm = Swarm(self.board, rows, cols,
                           h_spacing=1, v_spacing=1,
                           speed=1, color="green")

        # ———— Barriers
        self.barriers = [
            Barrier(self.board, bx, by)
            for bx, by in barrier_specs
        ]

        # ———— Audio & Effects
        snd_dir = os.path.join(base, "assets")
        self.snd = SoundManager(
            laser_file      = os.path.join(snd_dir, "lasers.wav"),
            explosion_file  = os.path.join(snd_dir, "explosion.wav"),
            game_over_file  = os.path.join(snd_dir, "game_over.wav")
        )

        # ———— Game state lists
        self.player_bullets = []
        self.invader_bombs  = []
        self.explosions     = []

        # ———— Controls
        self.master.bind("<Left>",  lambda e: self.player.move(-1))
        self.master.bind("<Right>", lambda e: self.player.move(1))
        self.master.bind("<space>", lambda e: self.fire())

        # ———— Loop timing
        self.delay = int(1000 / fps)
        self.tick()
        self.master.mainloop()


    def fire(self):
        """Player fires a bullet if none in flight."""
        b = self.player.fire()
        if b:
            self.player_bullets.append(b)
            self.snd.play_laser()


    def tick(self):
        """One frame: move, collisions, redraw, reschedule."""
        # 1) Move bullets & bombs
        for b in list(self.player_bullets):  b.move()
        for bomb in list(self.invader_bombs): bomb.move()
        self.player.update_bullets()   # cleans dead bullets

        # 1a) Move the swarm every N frames
        if not hasattr(self, "_swarm_tick"):
            self._swarm_tick   = 0
            self._swarm_period = 3
        self._swarm_tick += 1
        if self._swarm_tick >= self._swarm_period:
            self.swarm.move(self.board.grid_width)
            self._swarm_tick = 0

        # 2) Swarm randomly drops bombs
        if random.random() < 0.02:
            inv = self.swarm.random_invader()
            if inv:
                bomb = inv.drop_bomb()
                self.invader_bombs.append(bomb)

        # 3) Collisions
        self._handle_bullet_hits()
        self._handle_bomb_hits()

        # 4) Check win/loss
        if self.swarm.all_dead():
            return self._victory()
        if self.swarm.any_reached_bottom() or not self.player.alive:
            return self._game_over()

        # 5) Redraw everything
        self.board.clear()
        self.board.update_score(self.score, self.player.lives)
        for br in self.barriers:        br.draw()
        self.player.draw()
        for b in self.player_bullets:   b.draw()
        for bomb in self.invader_bombs:  bomb.draw()
        self.swarm.draw()
        for ex in list(self.explosions): pass  # explosions animate themselves

        # 6) Schedule next
        self.master.after(self.delay, self.tick)


    def _handle_bullet_hits(self):
        for b in list(self.player_bullets):
            bx, by = b.x, b.y
            if self.swarm.hit_invader_at(bx, by):
                b.hit()
                self.score += 10
                self.snd.play_explosion()
                self.explosions.append(Explosion(self.board, bx, by))
                continue
            for bar in self.barriers:
                if bar.hit(bx, by):
                    b.hit()
                    break


    def _handle_bomb_hits(self):
        for bomb in list(self.invader_bombs):
            bx, by = bomb.x, bomb.y
            for bar in self.barriers:
                if bar.hit(bx, by):
                    bomb.hit()
                    break
            if bomb.alive and self.player.contains(bx, by):
                bomb.hit()
                self.player.hit()
                self.snd.play_explosion()
                self.explosions.append(Explosion(self.board, bx, by))
                break


    def _victory(self):
        self.board.canvas.create_text(
            10*self.board.cell_size, 10*self.board.cell_size,
            text="YOU WIN!", fill="yellow", font=("Arial",32)
        )


    def _game_over(self):
        self.snd.play_game_over()
        cx = 10 * self.board.cell_size
        cy = 10 * self.board.cell_size

        # Main “Game Over” text
        self.board.canvas.create_text(
            cx, cy,
            text="GAME OVER", fill="red", font=("Arial",32)
        )
        # Restart prompt 
        self.board.canvas.create_text(
            cx, cy + 40,
            text="Press 'R' to play again",
            fill="white", font=("Arial",16)
        )
        # Bind 'r' to restart
        self.master.bind('r', lambda e: self._restart())


    def _restart(self):
        """Destroy current window and launch a fresh game."""
        self.master.destroy()
        SpaceInvaders()


if __name__ == "__main__":
    SpaceInvaders() 
