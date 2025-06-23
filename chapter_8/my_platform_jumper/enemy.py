# enemy.py

def update_enemies(enemies, platforms):
    for e in enemies:
        e['rect'].x += e['dir']*e['speed']
        if not any(e['rect'].colliderect(p) for p in platforms):
            e['dir'] *= -1
            e['rect'].x += e['dir']*e['speed']

def draw_enemies(surface, enemies, img, cam_x):
    for e in enemies:
        surface.blit(img, (e['rect'].x-cam_x, e['rect'].y))