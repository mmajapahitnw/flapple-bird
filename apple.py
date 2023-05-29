import pygame
from random import randint
from config import Config, State
from services import VisualService, sine

class Apple(pygame.sprite.Sprite):
    def __init__(self, y):
        super().__init__()
        self.start_y = y
        self.image = VisualService.get_apple()
        self.rect = self.image.get_rect(center=(randint(Config.WIDTH+26, Config.WIDTH+126), self.start_y))

    def update(self):
        self.rect.x -= 2
        self.rect.y = sine(200.0, 1280, 10, self.start_y)