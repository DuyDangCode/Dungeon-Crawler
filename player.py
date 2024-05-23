import pygame
import math


class Player:
    def __init__(self, x, y, image) -> None:
        self.image = image
        self.rec = pygame.Rect(0, 0, 50, 50)
        self.rec.center = (x, y)
        self.flip = False

    def update(self, dx, dy):
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

    def draw(self, surface, color):
        flipImage = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipImage, self.rec)
        pygame.draw.rect(surface, color, self.rec, 1)
