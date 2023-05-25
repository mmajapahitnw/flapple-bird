import pygame

class VisualService:
    @staticmethod
    def get_message():
        return pygame.image.load('sprites/message.png')

    @staticmethod
    def get_game_over():
        return pygame.image.load('sprites/gameover.png').convert_alpha()

    @staticmethod
    def get_bg_day():
        return pygame.image.load('sprites/background-day.png').convert()

    @staticmethod
    def get_bg_night():
        return pygame.image.load('sprites/background-night.png').convert()

    @staticmethod
    def get_ground():
        return pygame.image.load('sprites/base.png').convert()

    @staticmethod
    def get_yellowbird_upflap():
        return pygame.image.load('sprites/yellowbird-upflap.png').convert_alpha()

    @staticmethod
    def get_yellowbird_midflap():
        return pygame.image.load('sprites/yellowbird-midflap.png').convert_alpha()

    @staticmethod
    def get_yellowbird_downflap():
        return pygame.image.load('sprites/yellowbird-downflap.png').convert_alpha()

    @staticmethod
    def get_redbird_upflap():
        return pygame.image.load('sprites/redbird-upflap.png').convert_alpha()

    @staticmethod
    def get_redbird_midflap():
        return pygame.image.load('sprites/redbird-midflap.png').convert_alpha()

    @staticmethod
    def get_redbird_downflap():
        return pygame.image.load('sprites/redbird-downflap.png').convert_alpha()

    @staticmethod
    def get_bluebird_upflap():
        return pygame.image.load('sprites/bluebird-upflap.png').convert_alpha()

    @staticmethod
    def get_bluebird_midflap():
        return pygame.image.load('sprites/bluebird-midflap.png').convert_alpha()

    @staticmethod
    def get_bluebird_downflap():
        return pygame.image.load('sprites/bluebird-downflap.png').convert_alpha()

    @staticmethod
    def get_apple():
        return pygame.image.load('sprites/apple.png').convert_alpha()

    @staticmethod
    def get_green_pipe():
        return pygame.image.load('sprites/pipe-green.png').convert_alpha()

    @staticmethod
    def get_red_pipe():
        return pygame.image.load('sprites/pipe-red.png').convert_alpha()

    @staticmethod
    def get_icon():
        return pygame.image.load('favicon.ico').convert_alpha()


