
import pygame
from ui      import Button, TextLabel
from settings import BG_COLOR, SCREEN_WIDTH

class LauncherMenu:
    def __init__(self, options):

        self.title   = TextLabel("Select Mode", (SCREEN_WIDTH//2-100, 40))
        
        self.buttons = [
            Button(text, (SCREEN_WIDTH//2-100, 120 + i*70, 200, 50))
            for i, text in enumerate(options)
        ]

    def run(self, screen):
        clock = pygame.time.Clock()
        while True:
            screen.fill(BG_COLOR)
            self.title.draw(screen)
            for btn in self.buttons:
                btn.draw(screen)
            pygame.display.flip()
            clock.tick(60)

            for e in pygame.event.get():
                if e.type == pygame.QUIT:
                    return None
                for i, btn in enumerate(self.buttons):
                    if btn.is_clicked(e):
                        return i
