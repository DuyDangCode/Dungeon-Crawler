import pygame


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color, font):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(damage), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.count = 0

    def update(self, screenScroll):
        if self.count == 30:
            self.kill()
        self.rect.y -= 1
        self.count += 1
        self.rect.x += screenScroll[0]
        self.rect.y += screenScroll[1]

    def render(self, surface):
        surface.blit(self.image, self.rect)
