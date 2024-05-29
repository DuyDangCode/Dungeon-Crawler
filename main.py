from os import walk
from config import gameConstant, charactersConstant
import pygame
import sys
from item.coin import Coin, CoinIcon
from item.damageText import DamageText
from item.heart import Heart
from item.potionRed import PotionRed
from tile.world import World
from weapons.arrow import Arrow
from weapons.bow import Bow
import random

# pathWeaponsImage = "assets/images/weapons/"

pygame.init()
clock = pygame.time.Clock()
atariFont = pygame.font.Font(gameConstant.FONT_PATH_ATARI, gameConstant.FONT_SIZE)

pygame.display.set_caption(gameConstant.GAME_NAME)
screen = pygame.display.set_mode(
    (gameConstant.SCREEN_WIDTH, gameConstant.SCREEN_HEIGHT)
)


def drawGrid(screen):
    for i in range(30):
        pygame.draw.line(
            screen,
            gameConstant.WHITE,
            (i * gameConstant.TILE_SIZE, 0),
            (i * gameConstant.TILE_SIZE, gameConstant.SCREEN_HEIGHT),
        )
        pygame.draw.line(
            screen,
            gameConstant.WHITE,
            (0, i * gameConstant.TILE_SIZE),
            (gameConstant.SCREEN_WIDTH, i * gameConstant.TILE_SIZE),
        )


world = World(atariFont)

screenScroll = [0, 0]


def main():
    moving_up, moving_down, moving_right, moving_left = False, False, False, False
    while True:
        global screenScroll
        clock.tick(gameConstant.FPS)
        screen.fill(gameConstant.BACKGROUND)
        dx, dy = 0, 0
        if moving_up:
            dy += -gameConstant.SPEED
        if moving_down:
            dy += gameConstant.SPEED
        if moving_left:
            dx += -gameConstant.SPEED
        if moving_right:
            dx += gameConstant.SPEED
        world.update(dx, dy)
        world.render(screen)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
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


main()
