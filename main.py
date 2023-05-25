import pygame
from config import Config, State
from game_phases import menu_phase, gameplay_phase



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
            pass

        update_display()

if __name__ == '__main__':
    main()
