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

    def update(self, screenScroll, player):
        if pygame.time.get_ticks() - self.lastUpdateTime >= self.cooldown:
            self.indexFrame += 1
            if self.indexFrame == len(self.animationList):
                self.indexFrame = 0
            self.lastUpdateTime = pygame.time.get_ticks()

    def render(self, surface):
        surface.blit(self.animationList[self.indexFrame], self.rect)


class Coin(CoinIcon, pygame.sprite.Sprite):
    def __init__(self, x, y, sound):
        super().__init__(x, y)
        pygame.sprite.Sprite.__init__(self)
        self.sound = sound

    def update(self, screenScroll, player):
        if self.rect.colliderect(player.rect):
            player.score += 10 + random.randint(0, 10)
            self.sound.play()
            self.kill()
        self.rect.x += screenScroll[0]
        self.rect.y += screenScroll[1]
        super().update(screenScroll, None)

    def render(self, surface):
        super().render(surface)
