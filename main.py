import pygame
from config import Config, State
from functions import menu_phase, gameplay_phase, gameover_phase

frame_per_sec = pygame.time.Clock()

def update_display():
    pygame.display.update()
    frame_per_sec.tick(Config.FPS)

def main():
    pygame.init()

    while True:
        if State.game_state == 0:
            menu_phase()
        elif State.game_state == 1:
            gameplay_phase()
        elif State.game_state == 2:
            gameover_phase()

        update_display()

if __name__ == '__main__':
    main()
