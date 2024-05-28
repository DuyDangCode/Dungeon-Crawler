import pygame
import math
from config import gameConstant


class BaseCharacter:
    def __init__(self, x, y, animationList, health) -> None:
        self.indexFrame = 0
        self.action = 0
        self.updateFrameTime = pygame.time.get_ticks()
        self.animationList = animationList
        self.image = self.animationList[self.action][self.indexFrame]
        self.rect = pygame.Rect(0, 0, gameConstant.TILE_SIZE, gameConstant.TILE_SIZE)
        self.rect.center = (x, y)
        self.flip = False
        self.animationCooldown = 70
        self.health = health
        self.isALive = True

    def move(self, dx, dy):
        if dx != 0 or dy != 0:
            self.action = 1
        else:
            self.action = 0
        if dx < 0:
            self.flip = True
        elif dx > 0:
            self.flip = False

        if dx != 0 and dy != 0:
            dx = dx * (math.sqrt(2) / 2)
            dy = dy * (math.sqrt(2) / 2)
            # print(math.pow(dx, 2) + math.pow(dy, 2))
        self.rect.x += dx
        self.rect.y += dy

    def update(self):
        if pygame.time.get_ticks() - self.updateFrameTime > self.animationCooldown:
            self.indexFrame += 1
            self.updateFrameTime = pygame.time.get_ticks()
        if self.indexFrame == len(self.animationList):
            self.indexFrame = 0
        self.image = self.animationList[self.action][self.indexFrame]

    def render(self, surface, color):
        flipImage = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipImage, self.rect)
        pygame.draw.rect(surface, color, self.rect, 1)
