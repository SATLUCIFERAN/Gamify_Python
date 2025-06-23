# game.py
import pygame, sys
from settings import (
    SCREEN_WIDTH, SCREEN_HEIGHT, FPS, BG_COLOR,
    PLAYER_RUN_FRAMES, PLAYER_JUMP_FRAME, PLATFORM_IMAGE,
    COIN_IMAGE, ENEMY_IMAGE, BOSS_IMAGE, FIREBALL_IMAGE,
    TILE_SIZE, WORLD_WIDTH, START_X, START_Y,
    COIN_SCORE, COMBO_RESET_MS
)
from utils import load_and_scale, draw_text
from level import load_level, draw_level
from player import Player
from camera import Camera
import enemy
from boss import Sorcerer


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock  = pygame.time.Clock()

    # Load assets
    
    run_imgs   = [load_and_scale(f, TILE_SIZE) for f in PLAYER_RUN_FRAMES]
    jump_img   = load_and_scale(PLAYER_JUMP_FRAME, TILE_SIZE)
    plat_img   = load_and_scale(PLATFORM_IMAGE, TILE_SIZE)
    coin_img   = load_and_scale(COIN_IMAGE, TILE_SIZE // 2)
    enemy_img  = load_and_scale(ENEMY_IMAGE, TILE_SIZE)
    boss_img   = load_and_scale(BOSS_IMAGE, TILE_SIZE)
    fire_img   = load_and_scale(FIREBALL_IMAGE, 16)

    # Build world and entities
    platforms, coins, enemies = load_level()
    player   = Player(START_X, START_Y, run_imgs, jump_img)
    cam      = Camera()
    combo    = {'mult':0, 'last_time':0, 'score':0, 'base':COIN_SCORE, 'reset_ms':COMBO_RESET_MS}
    boss     = Sorcerer(boss_img)
    fireballs = []

    while True:
        dt  = clock.tick(FPS)
        now = pygame.time.get_ticks()

        for e in pygame.event.get():
            if e.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if not boss.victory and e.type == pygame.KEYDOWN and e.key == pygame.K_SPACE:
                if player.rect.colliderect(boss.rect) and boss.vulnerable:
                    boss.victory      = True
                    boss.victory_time = pygame.time.get_ticks()

        if not boss.victory:
            # Regular updates
            player.update(platforms)
            player.collect_coins(coins, now, combo)
            enemy.update_enemies(enemies, platforms)
            boss.update(now, fireballs, player.rect)
            for fb in fireballs[:]:
                fb.update()
                if (fb.rect.right < 0 or fb.rect.left > WORLD_WIDTH or
                    any(fb.rect.colliderect(p) for p in platforms)):
                    fireballs.remove(fb); continue
                if fb.rect.colliderect(player.rect):
                    player.rect.topleft = (START_X, START_Y)
                    player.vy           = 0
                    cam.offset_x        = 0
                    fireballs.remove(fb); continue
            if player.rect.top > SCREEN_HEIGHT or player.hit_enemies(enemies):
                player.rect.topleft = (START_X, START_Y)
                player.vy           = 0
                cam.offset_x        = 0
            cam.update(player.rect)
            

        # Draw everything
        screen.fill(BG_COLOR)
        draw_level(screen, platforms, plat_img, cam.offset_x)
        for c in coins:
            screen.blit(coin_img, (c.x - cam.offset_x, c.y))
        enemy.draw_enemies(screen, enemies, enemy_img, cam.offset_x)
        if not boss.victory:
            boss.draw(screen, cam.offset_x)
        for fb in fireballs:
            screen.blit(fire_img, (fb.rect.x - cam.offset_x, fb.rect.y))
        player.draw(screen, cam.offset_x)

        # Barrier at level end only
        # Prevent exiting the world before boss is defeated
        if not boss.victory and player.rect.right >= WORLD_WIDTH:
            player.rect.right = WORLD_WIDTH

        draw_text(screen, f"Score: {combo['score']} x{combo['mult']}", 24, 10, 10)

        # Blinking alert when in boss zone
        if not boss.victory and player.rect.centerx >= boss.rect.x - SCREEN_WIDTH:
            if (now // 500) % 2 == 0:
                font = pygame.font.SysFont(None, 36)
                alert_surf = font.render("ATTACK NOW! Press SPACE", True, (255, 0, 0))
                alert_rect = alert_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2))
                screen.blit(alert_surf, alert_rect)

        # Mission accomplished overlay
        if boss.victory:
            font = pygame.font.SysFont(None, 48)
            win_surf = font.render("MISSION ACCOMPLISHED!", True, (255, 215, 0))
            win_rect = win_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 - 20))
            screen.blit(win_surf, win_rect)
            sub_surf = font.render("Press ESC to Exit", True, (255, 255, 255))
            sub_rect = sub_surf.get_rect(center=(SCREEN_WIDTH//2, SCREEN_HEIGHT//2 + 20))
            screen.blit(sub_surf, sub_rect)
            keys = pygame.key.get_pressed()
            if keys[pygame.K_ESCAPE]:
                pygame.quit(); sys.exit()

        pygame.display.flip()

if __name__ == '__main__':
    main()