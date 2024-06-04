import pygame
from item.imageItem import imageItemInstance


class PotionRed(pygame.sprite.Sprite):
    def __init__(self, x, y, sound):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale_by(
            imageItemInstance.imagesList["potion_red"], 0.6
        )
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.sound = sound

    def update(self, screenScroll, player):
        if self.rect.colliderect(player) and player.health < 100:
            player.health += 10
            self.sound.play()
            self.kill()
        self.rect.x += screenScroll[0]
        self.rect.y += screenScroll[1]

    def render(self, surface):
        surface.blit(self.image, self.rect)
