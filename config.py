from pygame import display

class Config:
    FPS = 60
    WIDTH = 288
    HEIGHT = 512
    SCROLL = 0
    SCREEN = display.set_mode((WIDTH, HEIGHT))

class State:
    game_state = 0
    score = 0

