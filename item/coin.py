import pygame
from item.imageItem import imageItemInstance


class Coin:
    def __init__(self, x, y):
        self.animationList = []
        for i in range(4):
            self.animationList.append(imageItemInstance.imagesList[f"coin_f{i}"])
        self.indexFrame = 0
        self.lastUpdateTime = pygame.time.get_ticks()
        self.cooldown = 100
        self.rect = self.animationList[self.indexFrame].get_rect()
        self.rect.center = (x, y)

    def update(self):
        if pygame.time.get_ticks() - self.lastUpdateTime >= self.cooldown:
            self.indexFrame += 1
            if self.indexFrame == len(self.animationList):
                self.indexFrame = 0
            self.lastUpdateTime = pygame.time.get_ticks()

    def render(self, surface):
        self.update()
        surface.blit(self.animationList[self.indexFrame], self.rect)
