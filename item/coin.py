import pygame
from item.imageItem import imageItemInstance
import random


class CoinIcon:
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


class Coin(CoinIcon, pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        super().__init__(x, y)
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        # for i in range(4):
        #     self.animationList[i] = pygame.transform.scale_by(
        #         self.animationList[i], 0.5
        #     )

    def update(self):
        if self.rect.colliderect(self.player.rect):
            self.player.score += 10 + random.randint(0, 10)
            self.kill()
        super().update()

    def render(self, surface):
        super().render(surface)
