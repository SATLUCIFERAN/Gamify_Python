# player.py
import pygame
from settings import GRAVITY, JUMP_STRENGTH, MAX_FALL_SPEED, PLAYER_SPEED, START_X, START_Y, TILE_SIZE

class Player:
    def __init__(self, x=START_X, y=START_Y, run_imgs=None, jump_img=None):
        self.run_frames = run_imgs or []
        self.jump_frame = jump_img
        self.image      = self.run_frames[0] if self.run_frames else pygame.Surface((TILE_SIZE,TILE_SIZE))
        self.rect       = self.image.get_rect(topleft=(x,y))
        self.vx = self.vy = 0
        self.on_ground  = False
        self.anim_idx   = 0.0
        self.anim_spd   = 0.15

    def input(self):
        ks = pygame.key.get_pressed()
        self.vx = (ks[pygame.K_RIGHT] - ks[pygame.K_LEFT]) * PLAYER_SPEED
        if ks[pygame.K_SPACE] and self.on_ground:
            self.vy = JUMP_STRENGTH
            self.on_ground = False

    def physics(self, platforms):
        self.rect.x += self.vx
        for p in platforms:
            if self.rect.colliderect(p):
                self.rect.x -= self.vx
        self.vy = min(self.vy + GRAVITY, MAX_FALL_SPEED)
        self.rect.y += self.vy
        self.on_ground = False
        for p in platforms:
            if self.rect.colliderect(p):
                if self.vy > 0:
                    self.rect.bottom = p.top
                    self.vy = 0
                    self.on_ground = True
                elif self.vy < 0:
                    self.rect.top = p.bottom
                    self.vy = 0

    def animate(self):
        if not self.on_ground:
            self.image = self.jump_frame
        elif self.vx != 0 and self.run_frames:
            self.anim_idx = (self.anim_idx + self.anim_spd) % len(self.run_frames)
            self.image    = self.run_frames[int(self.anim_idx)]
        elif self.run_frames:
            self.image    = self.run_frames[0]

    def update(self, platforms):
        self.input()
        self.physics(platforms)
        self.animate()

    def collect_coins(self, coins, now, combo):
        for c in coins[:]:
            if self.rect.colliderect(c):
                coins.remove(c)
                if now - combo['last_time'] < combo['reset_ms']:
                    combo['mult'] += 1
                else:
                    combo['mult'] = 1
                combo['last_time'] = now
                combo['score'] += combo['mult'] * combo['base']

    def hit_enemies(self, enemies):
        return any(self.rect.colliderect(e['rect']) for e in enemies)
    

    def draw(self, surface, cam_x):
        surface.blit(self.image, (self.rect.x - cam_x, self.rect.y))