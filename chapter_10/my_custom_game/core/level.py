import json, pygame

class Level:
    def __init__(self, path):
        data = json.load(open(path))
        self.platforms = [pygame.Rect(*plat) for plat in data['platforms']]
        self.background_color = tuple(data['bg_color'])

    def draw(self, screen):
        for p in self.platforms:
            pygame.draw.rect(screen, (100,100,100), p)

    def update_enemies(self, player):
        # iterate enemies and update behavior
        pass

    def check_goal(self, rect):
        return rect.colliderect(pygame.Rect(*self.goal_area))