import pygame
from pygame.draw import rect
from config.gameConstant import BLACK, SCREEN_HEIGHT, SCREEN_WIDTH, WHITE, MAROON


class ScreenFade:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.cooldown = 20
        self.lastRenderTime = pygame.time.get_ticks()

    def render(self, surface, type):
        if type == 0:
            pygame.draw.rect(
                surface, BLACK, (-self.x, 0, SCREEN_WIDTH / 2, SCREEN_HEIGHT)
            )

            pygame.draw.rect(
                surface,
                BLACK,
                (SCREEN_WIDTH / 2 + self.x, 0, SCREEN_WIDTH / 2, SCREEN_HEIGHT),
            )
            pygame.draw.rect(
                surface, BLACK, (0, -self.y, SCREEN_WIDTH, SCREEN_HEIGHT / 2)
            )
            pygame.draw.rect(
                surface,
                BLACK,
                (0, SCREEN_HEIGHT / 2 + self.y, SCREEN_WIDTH, SCREEN_HEIGHT / 2),
            )
        else:
            tempSurface = pygame.Surface((SCREEN_WIDTH, self.y))
            tempSurface.set_alpha(128)
            tempSurface.fill(MAROON)
            surface.blit(tempSurface, (0, 0))

    def fade(self, surface, type):

        if type == 0:
            if (self.x > (SCREEN_WIDTH / 2)) or (self.y > (SCREEN_HEIGHT / 2)):
                self.x = 0
                self.y = 0
                return False
            self.render(surface, type)
            if pygame.time.get_ticks() - self.lastRenderTime > self.cooldown:
                self.x += 10
                self.y += 10
                self.lastRenderTime = pygame.time.get_ticks()

            return True
        if type == 1:
            self.render(surface, type)
            if self.y > SCREEN_HEIGHT:
                return
            if pygame.time.get_ticks() - self.lastRenderTime > self.cooldown:
                self.y += 10
                self.lastRenderTime = pygame.time.get_ticks()
