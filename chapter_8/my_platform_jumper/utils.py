# utils.py

import pygame, os, sys
from settings import ASSETS_DIR, TILE_SIZE

def load_and_scale(filename, size=TILE_SIZE):
    path = os.path.join(ASSETS_DIR, filename)
    if not os.path.isfile(path):
        sys.exit(f"Missing asset: {path}")
    img = pygame.image.load(path)
    w, h = img.get_size()
    factor = size / max(w, h)
    new_size = (int(w * factor), int(h * factor))
    try:
        return pygame.transform.scale(img.convert_alpha(), new_size)
    except pygame.error:
        return pygame.transform.scale(img.convert(), new_size)

def draw_text(surface, text, size, x, y, color=(255,255,255)):
    font = pygame.font.SysFont(None, size)
    surface.blit(font.render(text, True, color), (x, y))




