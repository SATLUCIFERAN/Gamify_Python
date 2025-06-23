
import pygame, importlib
from settings import SCREEN_WIDTH, SCREEN_HEIGHT
from menu     import LauncherMenu

CHAPTERS = [
    ("Multiplayer Server", "chapters.multiplayer_game.server", "main"),
    ("Multiplayer Client", "chapters.multiplayer_game.client", "main"),
]

def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    pygame.display.set_caption("Game Launcher")

    titles = [t for t,_,_ in CHAPTERS]
    choice = LauncherMenu(titles).run(screen)
    if choice is None:
        pygame.quit()
        return

    _, mod_path, fn_name = CHAPTERS[choice]
    module = importlib.import_module(mod_path)
    run_fn = getattr(module, fn_name)
    try:
        run_fn(screen)
    except TypeError:
        run_fn()
    pygame.quit()

if __name__ == "__main__":
    main()
