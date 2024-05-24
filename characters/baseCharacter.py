import pygame
import math


class BaseCharacter:
    def __init__(self, x, y, animationList) -> None:
        self.indexFrame = 0
        self.action = 0
        self.updateFrameTime = pygame.time.get_ticks()
        self.animationList = animationList
        self.image = self.animationList[self.action][self.indexFrame]
        self.rec = pygame.Rect(0, 0, 50, 50)
        self.rec.center = (x, y)
        self.flip = False
        self.animationCooldown = 70

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
        self.rec.x += dx
        self.rec.y += dy

    def updateAnimation(self):
        if pygame.time.get_ticks() - self.updateFrameTime > self.animationCooldown:
            self.indexFrame += 1
            self.updateFrameTime = pygame.time.get_ticks()
        if self.indexFrame == len(self.animationList):
            self.indexFrame = 0
        self.image = self.animationList[self.action][self.indexFrame]

    def render(self, surface, color):
        self.updateAnimation()
        flipImage = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipImage, self.rec)
        pygame.draw.rect(surface, color, self.rec, 1)
