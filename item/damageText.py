import pygame


class DamageText(pygame.sprite.Sprite):
    def __init__(self, x, y, damage, color, font):
        pygame.sprite.Sprite.__init__(self)
        self.image = font.render(str(damage), True, color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.count = 0

    def update(self):
        if self.count == 30:
            self.kill()
        self.rect.y -= 1
        self.count += 1

    def render(self, surface):
        self.update()
        surface.blit(self.image, self.rect)
