import pygame
from config import Config, State
from services import VisualService

class Pipe(pygame.sprite.Sprite):
    def __init__(self, rotation_index, y):
        super().__init__()
        self.pipe_images = [VisualService.get_green_pipe(), VisualService.get_red_pipe()]
        self.pipe_index = 0
        self.rotation_index = rotation_index
        if self.rotation_index == 0:
            self.image = self.pipe_images[self.pipe_index]
            self.rect = self.image.get_rect(topleft=(Config.WIDTH, y))
            # self.mask = pygame.mask.from_surface(self.image)
        elif self.rotation_index == 1:
            self.image = pygame.transform.flip(self.pipe_images[self.pipe_index], False, True)
            self.rect = self.image.get_rect(bottomleft=(Config.WIDTH, y))
            # self.mask = pygame.mask.from_surface(self.image)

    def update(self):
        self.rect.x -= 2
        if self.rect.right <= 0:
            State.score += 0.5
            self.kill()