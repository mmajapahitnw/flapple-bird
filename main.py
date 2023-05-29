import pygame
from config import Config, State
from functions import menu_phase, gameplay_phase, gameover_phase
from services import AudioService

frame_per_sec = pygame.time.Clock()

def update_display():
    pygame.display.update()
    frame_per_sec.tick(Config.FPS)

def main():
    pygame.init()
    bg_music = AudioService.get_music()
    bg_music.play(loops=-1)

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
