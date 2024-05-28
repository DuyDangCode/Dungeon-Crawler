import pygame
from item.imageItem import imageItemInstance


class PotionRed(pygame.sprite.Sprite):
    def __init__(self, x, y, player):
        pygame.sprite.Sprite.__init__(self)
        self.player = player
        self.image = pygame.transform.scale_by(
            imageItemInstance.imagesList["potion_red"], 0.6
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        if self.rect.colliderect(self.player) and self.player.health < 100:
            self.player.health += 10
            self.kill()

    def render(self, surface):
        self.update()
        surface.blit(self.image, self.rect)
