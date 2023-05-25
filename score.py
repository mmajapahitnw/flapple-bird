import pygame
from config import Config, State
from services import VisualService

class Score(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.numbers = [VisualService.get_zero(),
                        VisualService.get_one(),
                        VisualService.get_two(),
                        VisualService.get_three(),
                        VisualService.get_four(),
                        VisualService.get_five(),
                        VisualService.get_six(),
                        VisualService.get_seven(),
                        VisualService.get_eight(),
                        VisualService.get_nine()]
        self.score = 0
        self.width = self.numbers[0].get_width()
        self.spacing = 4
        self.digits = 1
        self.image = self.numbers[0]
        self.rect = self.image.get_rect(topleft=(300, 10))
        self.x = 10
        self.y = 10


    def update(self):
        self.score = int(State.score)

        self.digits = [int(digit) for digit in str(self.score)]
        for i, digit in enumerate(self.digits):
            self.image = self.numbers[digit]
            self.rect = self.image.get_rect(topright=(Config.WIDTH - self.x - (len(str(self.score)) - i - 1) * (self.width + self.spacing), self.y))
            Config.SCREEN.blit(self.image, self.rect)



