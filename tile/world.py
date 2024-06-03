import os

import pygame
from characters.bigDemon import BigDemon
from characters.elf import Elf
from characters.goblin import Goblin
from characters.imp import Imp
from characters.muddy import Muddy
from characters.skeleton import Skeleton
from characters.tinyZombie import TinyZombie
from item.coin import Coin, CoinIcon
from item.damageText import DamageText
from item.floor import Floor
from item.heart import Heart
from item.potionRed import PotionRed
from item.wall import Wall
from tile.imageTile import imageTileInstance
from config import gameConstant
import csv

from tile.screenFade import ScreenFade
from weapons.arrow import Arrow
from weapons.bow import Bow

pathLevel = "levels"


class World:
    def __init__(self, font):
        self.maps = {}
        for level in os.listdir(pathLevel):
            self.maps[str(level.split(".")[0])] = []
        for level in os.listdir(pathLevel):
            with open(f"{pathLevel}/{level}", newline="") as csvFile:
                reader = csv.reader(csvFile, delimiter=",")
                for row in reader:
                    data = []
                    for tile in row:
                        data.append(int(tile))
                    self.maps[str(level).split(".")[0]].append(data)
        self.level = 1
        self.gameOver = False
        self.scollXValue = 0
        self.scollYValue = 0
        self.floor = []
        self.wall = []
        self.enermies = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()
        self.damageText = pygame.sprite.Group()
        self.coinIcon = CoinIcon(gameConstant.SCREEN_WIDTH - 100, 25)
        self.font = font
        self.potionRed = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.process(self.level)

    def process(self, level):
        for y, row in enumerate(self.maps[str(level)]):
            for x, tileId in enumerate(row):
                if tileId == -1:
                    continue

                if tileId == 9:
                    self.coin.add(
                        Coin(gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y)
                    )
                elif tileId == 10:
                    self.potionRed.add(
                        PotionRed(
                            gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y
                        )
                    )
                elif tileId == 11:
                    self.player = Elf(
                        gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y
                    )
                    self.weapon = Bow(self.player.rect)
                    self.heart = Heart(self.player)
                elif tileId == 12:
                    self.enermies.add(
                        Imp(gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y)
                    )
                elif tileId == 13:
                    self.enermies.add(
                        Skeleton(gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y)
                    )
                elif tileId == 14:
                    self.enermies.add(
                        Goblin(gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y)
                    )
                elif tileId == 15:
                    self.enermies.add(
                        Muddy(gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y)
                    )
                elif tileId == 16:
                    self.enermies.add(
                        TinyZombie(
                            gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y
                        )
                    )
                elif tileId == 17:
                    self.enermies.add(
                        BigDemon(gameConstant.TILE_SIZE * x, gameConstant.TILE_SIZE * y)
                    )
                if tileId == 7:
                    self.wall.append(
                        Wall(
                            gameConstant.TILE_SIZE * x,
                            gameConstant.TILE_SIZE * y,
                            imageTileInstance.imageList[str(tileId)],
                        )
                    )
                else:
                    idFloor = 0
                    if tileId in range(0, 9):
                        idFloor = tileId
                    if tileId == 8:
                        self.checkPoint = pygame.Rect(
                            0, 0, gameConstant.TILE_SIZE, gameConstant.TILE_SIZE
                        )
                        self.checkPoint.center = (
                            x * gameConstant.TILE_SIZE,
                            y * gameConstant.TILE_SIZE,
                        )
                    self.floor.append(
                        Floor(
                            gameConstant.TILE_SIZE * x,
                            gameConstant.TILE_SIZE * y,
                            imageTileInstance.imageList[str(idFloor)],
                        )
                    )

    def resetLevel(self, level):
        self.scollXValue = 0
        self.scollYValue = 0
        self.floor = []
        self.wall = []
        self.enermies = pygame.sprite.Group()
        self.arrows = pygame.sprite.Group()
        self.damageText = pygame.sprite.Group()
        self.potionRed = pygame.sprite.Group()
        self.coin = pygame.sprite.Group()
        self.process(level)

    def uplevel(self):
        self.level += 1
        if self.level >= len(self.maps):
            self.level = len(self.maps) - 1
        self.resetLevel(self.level)

    def update(self, dx, dy):
        newLevel = False
        if not self.gameOver:
            self.player.move(dx, dy, self.wall)
            if self.player.health < 0:
                self.gameOver = True
            screenScroll = self.player.update2()
            self.checkPoint.x += screenScroll[0]
            self.checkPoint.y += screenScroll[1]

            if self.checkPoint.colliderect(self.player.rect):
                self.uplevel()
                newLevel = True
            else:
                newArrow = self.weapon.update()
                for damage in self.damageText:
                    damage.update(screenScroll)
                for enermy in self.enermies:
                    enermy.ai(self.player, self.wall)
                for enermy in self.enermies:
                    enermy.update(screenScroll)
                for potion in self.potionRed:
                    potion.update(screenScroll, self.player)
                for coin in self.coin:
                    coin.update(screenScroll, self.player)
                for arrow in self.arrows:
                    damage, damagePos = arrow.update2(
                        self.enermies, screenScroll, self.wall
                    )
                    if damage:
                        self.damageText.add(
                            DamageText(
                                damagePos[0],
                                damagePos[1],
                                damage,
                                gameConstant.RED,
                                self.font,
                            )
                        )
                if newArrow:
                    self.arrows.add(newArrow)
                for block in self.floor:
                    block.update(screenScroll)
                for block in self.wall:
                    block.update(screenScroll)
        return newLevel

    def drawInfo(self, surface):
        pygame.draw.line(
            surface, gameConstant.WHITE, (0, 50), (gameConstant.SCREEN_WIDTH, 50), 1
        )
        pygame.draw.rect(
            surface, gameConstant.PANEL, (0, 0, gameConstant.SCREEN_WIDTH, 50)
        )
        levelImage = self.font.render(
            "Level: " + str(self.level), True, gameConstant.WHITE
        )
        levelImageRect = levelImage.get_rect()
        levelImageRect.center = (gameConstant.SCREEN_WIDTH / 2, 25)
        surface.blit(levelImage, levelImageRect)
        self.heart.render(surface)
        self.coinIcon.render(surface)
        scoreImage = self.font.render(
            "x" + str(self.player.score), True, gameConstant.WHITE
        )
        surface.blit(scoreImage, (gameConstant.SCREEN_WIDTH - 80, 15))

    def render(self, surface):
        for block in self.floor:
            block.render(surface)
        for block in self.wall:
            block.render(surface)
        for enermy in self.enermies:
            enermy.render(surface, gameConstant.RED)
        for potion in self.potionRed:
            potion.render(surface)
        for coin in self.coin:
            coin.render(surface)
        self.player.render(surface, gameConstant.WHITE)
        self.weapon.render(surface)
        for damageText in self.damageText:
            damageText.render(surface)
        for arrow in self.arrows:
            arrow.render(surface)
        self.drawInfo(surface)
