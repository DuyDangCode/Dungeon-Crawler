import pygame
import math

from weapons.arrow import Arrow


class Bow:
    def __init__(self, rec, image, imageArrow):
        self.rec = rec
        self.angle = 0
        self.originalImage = image
        self.image = pygame.transform.rotate(self.originalImage, self.angle)
        self.imageArrow = imageArrow
        self.lastArrowTime = pygame.time.get_ticks()
        self.cooldownShoot = 300
        self.isShooting = False

    def update(self):

        x, y = pygame.mouse.get_pos()
        xDist = x - self.rec.centerx
        yDist = -(y - self.rec.centery)
        self.angle = math.degrees(math.atan2(yDist, xDist))
        arrow = None
        if (
            pygame.mouse.get_pressed()[0]
            and not self.isShooting
            and (pygame.time.get_ticks() - self.lastArrowTime) >= self.cooldownShoot
        ):
            arrow = Arrow(
                self.rec.centerx, self.rec.centery, self.angle, self.imageArrow
            )
            self.isShooting = True
        if not pygame.mouse.get_pressed()[0]:
            self.isShooting = False
        return arrow

    def render(self, surface):
        # print("center", self.rec.centerx)
        image = pygame.transform.rotate(self.originalImage, self.angle)
        surface.blit(
            image,
            (
                self.rec.centerx - int(self.image.get_width() / 2),
                self.rec.centery - int(self.image.get_height() / 2),
            ),
        )
