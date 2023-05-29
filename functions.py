import pygame
from random import randint
from player import Player
from pipe import Pipe
from apple import Apple
from score import Score
import services
from config import Config, State

screen = Config.SCREEN
pygame.display.set_caption('flapple bird')
icon = services.VisualService.get_icon()
pygame.display.set_icon(icon)

screen = Config.SCREEN

# adds timer for events
pipe_timer = pygame.USEREVENT + 1
pygame.time.set_timer(pipe_timer, 2000)
apple_timer = pygame.USEREVENT + 2
pygame.time.set_timer(apple_timer, 8000)

P1 = Player()
player = pygame.sprite.GroupSingle()
player.add(P1)

pipes = pygame.sprite.Group()

apple = pygame.sprite.Group(Apple(300))

scores = pygame.sprite.GroupSingle(Score())

def move_scroll(scroll):
    scroll -= 2
    if scroll <= -24:
        scroll = 0
    return scroll

def moving_ground(screen, scroll):
    screen.blit(services.VisualService.get_ground(), (scroll, Config.HEIGHT-100))

def check_pipe_collisions():
    if pygame.sprite.spritecollide(P1, pipes, False, pygame.sprite.collide_mask):
        State.game_state = 2
        services.AudioService.get_hit().play()
    if player.sprite.rect.bottom >= 403 or player.sprite.rect.top < -150:
        State.game_state = 2
        services.AudioService.get_hit().play()

def check_apple_collision():
    pygame.sprite.groupcollide(apple, pipes, True, False)
    if pygame.sprite.spritecollide(P1, apple, True):
        State.score += 5
        State.apple_event = pygame.time.get_ticks()
        State.apple_jumpstart = 0
        services.AudioService.get_apple().play()

def menu_phase():
    # display backgorund
    screen.blit(services.VisualService.get_bg_day(), (0, 0))

    # display moving ground
    Config.SCROLL = move_scroll(Config.SCROLL)
    moving_ground(screen, Config.SCROLL)

    # display message
    message_surf = services.VisualService.get_message()
    message_rect = message_surf.get_rect(center=(Config.WIDTH // 2, Config.HEIGHT // 2))
    screen.blit(message_surf, message_rect)

    # event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            State.game_state = 1
        if event.type == pygame.MOUSEBUTTONDOWN:
            State.game_state = 1

def gameplay_phase():
    # display backgorund
    if State.daytime:
        screen.blit(services.VisualService.get_bg_day(), (0, 0))
    else:
        screen.blit(services.VisualService.get_bg_night(), (0, 0))

    # day and night cycle
    if (State.score // 10) % 2 == 0:
        State.daytime = True
    else:
        State.daytime = False

    # apple mode
    if (pygame.time.get_ticks() - State.apple_event + State.apple_jumpstart) >= State.apple_duration:
        # is game over
        check_pipe_collisions()
    else:
        pass

    pipes.draw(screen)
    pipes.update()

    # display moving ground
    Config.SCROLL = move_scroll(Config.SCROLL)
    moving_ground(screen, Config.SCROLL)

    player.draw(screen)
    player.update()

    apple.draw(screen)
    apple.update()

    scores.draw(screen)
    scores.update()

    check_apple_collision()

    # event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()

        if event.type == pipe_timer:
            y = randint(50 + Config.PIPE_GAP, Config.HEIGHT - 100 - 50)
            pipes.add(Pipe(0, y, State.pipe_color))
            pipes.add(Pipe(1, y-Config.PIPE_GAP, State.pipe_color))

        if event.type == apple_timer:
            y = randint(100, Config.HEIGHT - 200)
            apple.add(Apple(y))

def gameover_phase():
    # event loops
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            exit()
        if event.type == pygame.MOUSEBUTTONDOWN or (event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE):
            State.game_state = 1
            pipes.empty()
            apple.empty()
            State.score = 0
            State.game_state = 1
            P1.rect.y = (Config.HEIGHT-100)//2
            State.pipe_color=randint(0,1)
    screen.blit(services.VisualService.get_game_over(), (Config.WIDTH // 2 - services.VisualService.get_game_over().get_width() // 2,
                                                         Config.HEIGHT // 2 - services.VisualService.get_game_over().get_height() // 2))







