import pygame
from weapons.imageWeapons import imageWeaponInstance
import math
from config import gameConstant


class FireBall(pygame.sprite.Sprite):
    def __init__(self, x, y, xTarget, yTarget):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageWeaponInstance.imageLists["fireball"]
        self.rect = self.image.get_rect()
        self.rect.centerx = x
        self.rect.centery = y
        self.angle = math.atan2(
            -(yTarget - self.rect.centery), (xTarget - self.rect.centerx)
        )
        self.dx = math.cos(self.angle) * gameConstant.ARROW_SPEED * 2
        self.dy = -math.sin(self.angle) * gameConstant.ARROW_SPEED * 2

    def update(self, screenScroll):
        self.rect.centerx += self.dx + screenScroll[0]
        self.rect.centery += self.dy + screenScroll[1]
        if (
            self.rect.right < 0
            or self.rect.left > gameConstant.SCREEN_WIDTH
            or self.rect.top > gameConstant.SCREEN_HEIGHT
            or self.rect.bottom < 0
        ):
            self.kill()

    def render(self, surface):
        surface.blit(self.image, self.rect)
