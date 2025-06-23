
import pygame

class TextLabel:
    def __init__(self, text, pos, font_size=36):
        self.font = pygame.font.SysFont(None, font_size)
        self.img  = self.font.render(text, True, (240,240,240))
        self.pos  = pos

    def draw(self, surf):
        surf.blit(self.img, self.pos)

class Button:
    def __init__(self, text, rect, font_size=28):
        self.rect  = pygame.Rect(rect)
        self.label = TextLabel(text, (self.rect.x+10, self.rect.y+10), font_size)

    def draw(self, surf):
        pygame.draw.rect(surf, (70,70,70), self.rect)
        pygame.draw.rect(surf, (200,200,200), self.rect, 2)
        self.label.draw(surf)

    def is_clicked(self, event):
        return event.type == pygame.MOUSEBUTTONDOWN and self.rect.collidepoint(event.pos)
