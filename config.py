from pygame import display

class Config:
    FPS = 60
    WIDTH = 288
    HEIGHT = 512
    SCROLL = 0
    SCREEN = display.set_mode((WIDTH, HEIGHT))
    PIPE_GAP = 125

class State:
    game_state = 0
    score = 0
    daytime = True
    apple_event = 0
    apple_duration = 2000
    apple_phase_time = 100
    apple_jumpstart = apple_duration
    pipe_color = 0

