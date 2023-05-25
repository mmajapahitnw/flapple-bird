import pygame
from random import randint
from player import Player
from pipe import Pipe
import services
from config import Config, State

screen = pygame.display.set_mode((Config.WIDTH, Config.HEIGHT))
pygame.display.set_caption('flapple bird')
icon = services.VisualService.get_icon()
pygame.display.set_icon(icon)

pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 4500)

P1 = Player()
player = pygame.sprite.GroupSingle()
player.add(P1)

pipes = pygame.sprite.Group()

def move_scroll(scroll):
    scroll -= 1
    if scroll <= -24:
        scroll = 0
    return scroll

def moving_ground(screen, scroll):
    screen.blit(services.VisualService.get_ground(), (scroll, Config.HEIGHT-100))

def menu_phase():
    # display backgorund
    screen.blit(services.VisualService.get_bg_day(), (0, 0))

    # display message
    message_surf = services.VisualService.get_message()
    pygame.transform.rotozoom(message_surf, 0, 1.5)
    message_rect = message_surf.get_rect(center=(Config.WIDTH//2, Config.HEIGHT//2))
    screen.blit(message_surf, message_rect)

    # display moving ground
    Config.SCROLL = move_scroll(Config.SCROLL)
    moving_ground(screen, Config.SCROLL)

    # event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if pygame.mouse.get_pressed()[0]:
            State.game_state = 1

def gameplay_phase():
    # display backgorund
    screen.blit(services.VisualService.get_bg_day(), (0, 0))

    player.draw(screen)
    player.update()

    pipes.draw(screen)
    pipes.update()

    # display moving ground
    Config.SCROLL = move_scroll(Config.SCROLL)
    moving_ground(screen, Config.SCROLL)

    # event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            print('space')
        if event.type == pipe_timer:
            y = randint(212, 312)
            pipes.add(Pipe(0, y))
            pipes.add(Pipe(1, y-100))






