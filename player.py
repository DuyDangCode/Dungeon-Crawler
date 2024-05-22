import pygame


class Player:
    def __init__(self, x, y) -> None:
        self.rec = pygame.Rect(0, 0, 50, 50)
        self.rec.center = (x, y)

    def draw(self, surface, color):
        pygame.draw.rect(surface, color, self.rec)
