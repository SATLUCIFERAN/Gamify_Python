# settings.py
import os

# Window dimensions
SCREEN_WIDTH   = 800
SCREEN_HEIGHT  = 600
FPS            = 60

# Tile grid (world size)
TILE_SIZE      = 40
TILE_COLS      = 100
TILE_ROWS      = 15

# World & camera bounds
WORLD_WIDTH    = TILE_COLS * TILE_SIZE
WORLD_HEIGHT   = TILE_ROWS * TILE_SIZE
MAX_CAM_X      = max(0, WORLD_WIDTH - SCREEN_WIDTH)


# Colors
BG_COLOR       = (135, 206, 235)  # sky blue

# Physics & movement

GRAVITY        = 0.5
JUMP_STRENGTH  = -12
MAX_FALL_SPEED = 10
PLAYER_SPEED   = 5

# Spawn point (respawn)
START_X        = 100
START_Y        = SCREEN_HEIGHT - 2 * TILE_SIZE

# Scoring
COIN_SCORE     = 10         # base score per coin
COMBO_RESET_MS = 1500       # ms before combo resets

# Boss encounter
BOSS_IMAGE      = 'sorcerer.png'
FIREBALL_IMAGE  = 'fireball.png'
FIREBALL_SPEED  = 6
SHOOT_INTERVAL  = 2000      # ms between shots
VULNERABLE_TIME = 1500      # ms boss is vulnerable after each shot
BOSS_X          = WORLD_WIDTH - 6 * TILE_SIZE
BOSS_Y          = (TILE_ROWS - 4) * TILE_SIZE

# Asset paths
BASE_DIR         = os.path.dirname(__file__)
ASSETS_DIR       = os.path.join(BASE_DIR, 'assets')
PLAYER_RUN_FRAMES = ['player_run1.png', 'player_run2.png']
PLAYER_JUMP_FRAME = 'player_jump.png'
PLATFORM_IMAGE    = 'platform.png'
COIN_IMAGE        = 'coin.png'
ENEMY_IMAGE       = 'enemy.png'