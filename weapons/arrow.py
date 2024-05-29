import pygame
import math
from config import gameConstant
import random

from item.damageText import DamageText


class Arrow(pygame.sprite.Sprite):
    def __init__(self, x, y, angle, image):
        pygame.sprite.Sprite.__init__(self)
        self.originalImage = image
        self.angle = angle
        self.image = pygame.transform.rotate(self.originalImage, self.angle - 90)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.dx = math.cos(math.radians(self.angle)) * gameConstant.ARROW_SPEED
        self.dy = -math.sin(math.radians(self.angle)) * gameConstant.ARROW_SPEED

    def update2(self, enermies, screenScroll, walls):
        damage = 0
        damagePos = None
        self.rect.x += int(self.dx) + screenScroll[0]
        self.rect.y += int(self.dy) + screenScroll[1]
        if (
            self.rect.top > gameConstant.SCREEN_HEIGHT
            or self.rect.bottom < 0
            or self.rect.left > gameConstant.SCREEN_WIDTH
            or self.rect.right < 0
        ):
            self.kill()

        for enermy in enermies:
            if self.rect.colliderect(enermy.rect) and enermy.isALive:
                damage = 10 + random.randint(0, 10)
                enermy.health -= damage
                damagePos = (enermy.rect.centerx, enermy.rect.centery)

                self.kill()
                if enermy.health < 0:
                    enermy.isALive = False
        for wall in walls:
            if wall.rect.colliderect(self.rect):
                self.kill()
        return damage, damagePos

    def render(self, surface):
        surface.blit(self.image, (self.rect.centerx, self.rect.centery))
