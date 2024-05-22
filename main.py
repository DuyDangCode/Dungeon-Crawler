import pygame
from config import constant
from player import Player

pygame.init()
screen = pygame.display.set_mode((constant.SCREEN_WIDTH, constant.SCREEN_HEIGHT))
player = Player(100, 100)
run = True
pygame.display.set_caption(constant.GAME_NAME)


while run:
    player.draw(screen, constant.WHITE)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
