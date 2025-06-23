import pygame
from settings import GRAVITY, JUMP_POWER, PLAYER_SPEED

class Player:
    def __init__(self, x, y):
        self.image = pygame.image.load('assets/player.png')
        self.rect = self.image.get_rect(topleft=(x,y))
        self.vel_y = 0

    def handle_input(self, event):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT]: self.rect.x -= PLAYER_SPEED
        if keys[pygame.K_RIGHT]: self.rect.x += PLAYER_SPEED
        if keys[pygame.K_SPACE] and self.on_ground:
            self.vel_y = -JUMP_POWER

    def update(self, platforms):
        # Apply gravity
        self.vel_y += GRAVITY
        self.rect.y += self.vel_y
        # Check collisions with platforms
        for p in platforms:
            if self.rect.colliderect(p):
                # Simple landing logic
                if self.vel_y > 0:
                    self.rect.bottom = p.top
                    self.vel_y = 0
                    self.on_ground = True