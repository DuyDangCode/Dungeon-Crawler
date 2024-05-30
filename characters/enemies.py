import math

import pygame
from characters.baseCharacter import BaseCharacter
from config import gameConstant
import random


class Enemies(BaseCharacter):
    def __init__(self, x, y, animationList, health):
        super().__init__(x, y, animationList, health)
        self.lastHitTime = pygame.time.get_ticks()
        self.colldowns = 300

    def ai(self, player, walls):

        dx = 0
        dy = 0

        dict = math.sqrt(
            (self.rect.centerx - player.rect.centerx) ** 2
            + (self.rect.centery - player.rect.centery) ** 2
        )
        lineSight = (
            (self.rect.centerx, self.rect.centery),
            (player.rect.centerx, player.rect.centery),
        )
        seePlayer = True
        for wall in walls:
            line = wall.rect.clipline(lineSight)
            if line:
                seePlayer = False
                break
        if seePlayer:
            # print(dict)
            extraSpeed = 0
            if (
                self.rect.colliderect(player.rect)
                and (pygame.time.get_ticks() - self.lastHitTime) > self.colldowns
            ):
                player.health -= random.randint(0, 30)
                self.lastHitTime = pygame.time.get_ticks()
            if dict < 100:
                extraSpeed = 1
            if dict > gameConstant.RANGE_BETWEEN_CHARACTER:
                if self.rect.centerx - player.rect.centerx < 0:
                    dx = gameConstant.MIN_SPEED_ENERMIES + extraSpeed
                if self.rect.centerx - player.rect.centerx > 0:
                    dx = -(gameConstant.MIN_SPEED_ENERMIES + extraSpeed)
                if self.rect.centery - player.rect.centery < 0:
                    dy = gameConstant.MIN_SPEED_ENERMIES + extraSpeed
                if self.rect.centery - player.rect.centery > 0:
                    dy = -(gameConstant.MIN_SPEED_ENERMIES + extraSpeed)

        self.move(dx, dy, walls)
