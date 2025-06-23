# camera.py
from settings import SCREEN_WIDTH, MAX_CAM_X

class Camera:
    def __init__(self):
        self.offset_x = 0

    def update(self, target_rect):
        desired = target_rect.centerx - SCREEN_WIDTH // 2
        self.offset_x = max(0, min(desired, MAX_CAM_X))