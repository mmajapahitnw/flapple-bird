import pygame
from config import Config
from services import VisualService

class Pipe(pygame.sprite.Sprite):
    def __init__(self, rotation_index, y):
        super().__init__()
        self.pipe_images = [[VisualService.get_green_pipe(), pygame.transform.rotozoom(VisualService.get_green_pipe(), 180, 1)],
                            [VisualService.get_red_pipe(), pygame.transform.rotozoom(VisualService.get_red_pipe(), 180, 1)]]
        self.pipe_index = 0
        self.rotation_index = rotation_index
        self.image = self.pipe_images[self.pipe_index][self.rotation_index]
        if self.rotation_index == 0:
            self.rect = self.image.get_rect(topleft=(Config.WIDTH, y))
        elif self.rotation_index == 1:
            self.rect = self.image.get_rect(bottomleft=(Config.WIDTH, y))

    def update(self):
        self.rect.x -= 1