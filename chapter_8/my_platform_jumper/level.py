# level.py
import pygame
from settings import TILE_SIZE, TILE_COLS, TILE_ROWS

def load_level():
    platforms, coins, enemies = [], [], []

    # Ground with pits every 10 tiles
    for col in range(TILE_COLS):
        if (col % 10) in (8, 9): continue
        platforms.append(pygame.Rect(col*TILE_SIZE, (TILE_ROWS-1)*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Floating & elevated platforms
    
    for base in range(0, TILE_COLS, 10):
        for dx in (7, 9):
            x = (base + dx) * TILE_SIZE
            y = (TILE_ROWS - 4) * TILE_SIZE
            platforms.append(pygame.Rect((base+dx)*TILE_SIZE, (TILE_ROWS-4)*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Mid-level extras
    for x in range(5, TILE_COLS, 15):
        for y in (6, 9):
            platforms.append(pygame.Rect(x*TILE_SIZE, y*TILE_SIZE, TILE_SIZE, TILE_SIZE))

    # Elevated ledges
    for pos in (12, 30, 55, 75):
        for dy in (5, 6):
            x = pos * TILE_SIZE
            y = (TILE_ROWS - dy) * TILE_SIZE
            platforms.append(pygame.Rect(x, y, TILE_SIZE, TILE_SIZE))


    # Coins atop every non-ground platform
    coin_size = TILE_SIZE // 2
    ground_y  = (TILE_ROWS - 1) * TILE_SIZE

    for p in platforms:
        if p.y == ground_y:
            continue
        cx = p.x + (TILE_SIZE - coin_size) // 2
        cy = p.y - coin_size - 30
        coins.append(pygame.Rect(cx, cy, coin_size, coin_size))

    # Enemies patrolling
    for p in platforms[::20]:
        er = pygame.Rect(p.x, p.y - TILE_SIZE, TILE_SIZE, TILE_SIZE)
        enemies.append({'rect': er, 'dir': 1, 'speed': 2})

    return platforms, coins, enemies

def draw_level(surface, platforms, img, cam_x):
    for p in platforms:
        surface.blit(img, (p.x-cam_x, p.y))