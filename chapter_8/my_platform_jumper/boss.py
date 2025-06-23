# boss.py
import pygame, math
from settings import BOSS_X, BOSS_Y, SHOOT_INTERVAL, VULNERABLE_TIME, FIREBALL_SPEED

class Fireball:
    def __init__(self, x, y, vx, vy):
        self.rect = pygame.Rect(x, y, 16, 16)
        self.vx   = vx
        self.vy   = vy

    def update(self):
        self.rect.x += self.vx
        self.rect.y += self.vy

class Sorcerer:
    def __init__(self, image):
        self.image       = image
        self.rect        = self.image.get_rect(topleft=(BOSS_X, BOSS_Y))
        self.last_shot   = 0
        self.vulnerable  = False
        self.vuln_timer  = 0
        self.victory     = False  
        self.victory_time= 0

    def update(self, now, fireballs, player_rect):
        if now - self.last_shot >= SHOOT_INTERVAL:
            sx, sy = self.rect.center
            px, py = player_rect.center
            dx, dy = px - sx, py - sy
            dist   = math.hypot(dx, dy) or 1
            vx = dx / dist * FIREBALL_SPEED
            vy = dy / dist * FIREBALL_SPEED
            fireballs.append(Fireball(sx, sy, vx, vy))
            self.last_shot  = now
            self.vulnerable = True
            self.vuln_timer = now
        if self.vulnerable and now - self.vuln_timer >= VULNERABLE_TIME:
            self.vulnerable = False

    def draw(self, surface, cam_x):
        img = self.image.copy()
        if self.vulnerable:
            img.fill((255, 255, 0), special_flags=pygame.BLEND_ADD)
        surface.blit(img, (self.rect.x - cam_x, self.rect.y))