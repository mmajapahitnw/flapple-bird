import pygame
from config import Config, State
from services import VisualService

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        yellowbird_images = [VisualService.get_yellowbird_upflap(),
                             VisualService.get_yellowbird_midflap(),
                             VisualService.get_yellowbird_downflap()]
        redbird_images = [VisualService.get_redbird_upflap(),
                          VisualService.get_redbird_midflap(),
                          VisualService.get_redbird_downflap()]
        bluebird_images = [VisualService.get_bluebird_upflap(),
                           VisualService.get_bluebird_midflap(),
                           VisualService.get_bluebird_downflap()]
        self.bird_images = [yellowbird_images, redbird_images, bluebird_images]
        self.flap_index = 0
        self.bird_index = 0
        self.image = self.bird_images[self.bird_index][self.flap_index]
        self.rect = self.image.get_rect(center=(50, (Config.HEIGHT-100)//2))
        self.mask = pygame.mask.from_surface(self.image)

        self.gravity = 0
        self.jump_height = 5


    def player_input(self):
        if pygame.mouse.get_pressed()[0] or pygame.key.get_pressed()[pygame.K_SPACE]:
            self.gravity = -self.jump_height



    def apply_gravity(self):
        self.gravity += 0.4
        self.rect.y += self.gravity
        if self.gravity >= self.jump_height:
            self.gravity = self.jump_height

    def animation(self):
        if self.gravity < -2:
            self.flap_index = 0
            self.image = pygame.transform.rotozoom(self.bird_images[self.bird_index][self.flap_index], -self.gravity*60/self.jump_height, 1)
            self.mask = pygame.mask.from_surface(self.image)
        elif -2 <= self.gravity <= 2:
            self.flap_index = 1
            self.image = pygame.transform.rotozoom(self.bird_images[self.bird_index][self.flap_index], -self.gravity*60/self.jump_height, 1)
            self.mask = pygame.mask.from_surface(self.image)
        elif self.gravity > 2:
            self.image = pygame.transform.rotozoom(self.bird_images[self.bird_index][self.flap_index], -self.gravity*60/self.jump_height, 1)
            self.mask = pygame.mask.from_surface(self.image)



    def update(self):
        self.player_input()
        self.apply_gravity()
        if (pygame.time.get_ticks() - State.apple_event + State.apple_jumpstart) >= State.apple_duration:
            self.bird_index = 0
            self.animation()
        else:
            if ((pygame.time.get_ticks() - State.apple_event) // State.apple_phase_time) % 3 == 0:
                self.bird_index = 1
            elif ((pygame.time.get_ticks() - State.apple_event) // State.apple_phase_time) % 3 == 1:
                self.bird_index = 2
            else:
                self.bird_index = 0
            self.animation()
