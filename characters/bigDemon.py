import pygame
from characters.enemies import Enemies
from characters.imageCharacter import imageFacotry
from config.gameConstant import HEALTH, TILE_SIZE, SCALE
from weapons.fireball import FireBall


class BigDemon(Enemies):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            imageFacotry.imageLists["big_demon"].playerAnimationList,
            HEALTH,
        )
        self.fireBalls = pygame.sprite.Group()
        self.coolDownsFireBalls = 500
        self.lastHitTime = pygame.time.get_ticks()
        self.rect = pygame.Rect(0, 0, TILE_SIZE * 1.2, TILE_SIZE * 2)
        self.rect.center = (x, y)
        self.offSet = 8
        self.health = 500

    def ai(self, player, walls):
        super().ai(player, walls)
        if self.seePlayer and (
            pygame.time.get_ticks() - self.lastHitTime > self.coolDownsFireBalls
        ):
            self.fireBalls.add(
                FireBall(
                    self.rect.centerx,
                    self.rect.centery,
                    player.rect.centerx,
                    player.rect.centery,
                )
            )
            self.lastHitTime = pygame.time.get_ticks()
        for fireBall in self.fireBalls:
            if fireBall.rect.colliderect(player.rect):
                player.health -= 10
                fireBall.kill()

    def update(self, screenScroll):
        for fireball in self.fireBalls:
            fireball.update(screenScroll)
        super().update(screenScroll)

    def render(self, surface, color):
        for fireball in self.fireBalls:
            fireball.render(surface)
        flipImage = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(flipImage, (self.rect.x - self.offSet * SCALE, self.rect.y))
        pygame.draw.rect(surface, color, self.rect, 1)
