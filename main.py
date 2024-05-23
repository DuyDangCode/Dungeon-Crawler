import pygame
from config import constant
from player import Player
from utils.utils import scaleImage

pygame.init()

clock = pygame.time.Clock()
pygame.display.set_caption(constant.GAME_NAME)

screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))

playerImage = pygame.image.load(
    "assets/images/characters/elf/idle/0.png"
).convert_alpha()
playerImage = scaleImage(playerImage, constant.SCALE)
player = Player(100, 100, playerImage)

run = True

moving_up, moving_down, moving_right, moving_left = False, False, False, False

while run:
    clock.tick(constant.FPS)
    screen.fill(constant.BACKGROUND)
    dx, dy = 0, 0
    if moving_up:
        dy += -constant.SPEED
    if moving_down:
        dy += constant.SPEED
    if moving_left:
        dx += -constant.SPEED
    if moving_right:
        dx += constant.SPEED

    player.update(dx, dy)
    player.draw(screen, constant.WHITE)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_a:
                moving_left = True
            if event.key == pygame.K_w:
                moving_up = True
            if event.key == pygame.K_d:
                moving_right = True
            if event.key == pygame.K_s:
                moving_down = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_a:
                moving_left = False
            if event.key == pygame.K_w:
                moving_up = False
            if event.key == pygame.K_d:
                moving_right = False
            if event.key == pygame.K_s:
                moving_down = False

    pygame.display.update()

pygame.quit()
