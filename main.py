from os import walk
from config import gameConstant, charactersConstant
import pygame
import sys
from item.coin import Coin
from item.damageText import DamageText
from item.heart import Heart
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

player = charactersConstant.charactersLists["elf"](100, 100)
weapon = Bow(player.rect)

arrowGroup = pygame.sprite.Group()
enermies = []
enermies.append(
    charactersConstant.charactersLists[charactersConstant.bigDemonName](
        random.randint(100, 300), random.randint(100, 300)
    )
)
enermies.append(
    charactersConstant.charactersLists[charactersConstant.skeletonName](
        random.randint(100, 300), random.randint(100, 300)
    )
)

damageTextGroup = pygame.sprite.Group()

heart = Heart(player)
coin = Coin(gameConstant.SCREEN_WIDTH - 100, 25)


def drawInfo(screen):
    pygame.draw.line(
        screen, gameConstant.WHITE, (0, 50), (gameConstant.SCREEN_WIDTH, 50), 1
    )
    pygame.draw.rect(screen, gameConstant.PANEL, (0, 0, gameConstant.SCREEN_WIDTH, 50))
    heart.render(screen)
    coin.render(screen)
    scoreImage = atariFont.render("x00", True, gameConstant.WHITE)
    screen.blit(scoreImage, (gameConstant.SCREEN_WIDTH - 80, 15))


def main():
    moving_up, moving_down, moving_right, moving_left = False, False, False, False
    while True:
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

        player.move(dx, dy)
        player.update()

        for arrow in arrowGroup:
            damage, damagePos = arrow.update2(enermies)
            if damage:
                damageTextGroup.add(
                    DamageText(
                        damagePos[0],
                        damagePos[1],
                        damage,
                        gameConstant.RED,
                        atariFont,
                    )
                )

        newArrow = weapon.update()

        if newArrow:
            arrowGroup.add(newArrow)

        player.render(screen, gameConstant.WHITE)
        weapon.render(screen)
        for enermy in enermies:
            enermy.render(screen, gameConstant.RED)
            # print(enermy.health)
        for damageText in damageTextGroup:
            damageText.render(screen)

        for arrow in arrowGroup:
            arrow.render(screen)

        drawInfo(screen)
        # print("arrows::", arrowGroup)

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
