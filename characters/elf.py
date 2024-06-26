import pygame
from pygame.display import set_allow_screensaver
from characters.baseCharacter import BaseCharacter
from characters.imageCharacter import imageFacotry
from config import gameConstant
from weapons.arrow import Arrow


class Elf(BaseCharacter):
    def __init__(self, x, y):
        self.offSet = 12
        self.score = 0
        super().__init__(
            x,
            y,
            imageFacotry.imageLists["elf"].playerAnimationList,
            100,
        )

    def update2(self):
        screenScroll = [0, 0]
        super().update(screenScroll)
        if self.rect.right > (gameConstant.SCREEN_WIDTH - gameConstant.THRESHOLD_X):
            screenScroll[0] = (
                gameConstant.SCREEN_WIDTH - gameConstant.THRESHOLD_X - self.rect.right
            )
            self.rect.right = gameConstant.SCREEN_WIDTH - gameConstant.THRESHOLD_X

        if self.rect.left < gameConstant.THRESHOLD_X:
            screenScroll[0] = gameConstant.THRESHOLD_X - self.rect.left
            self.rect.left = gameConstant.THRESHOLD_X

        if self.rect.bottom > (gameConstant.SCREEN_HEIGHT - gameConstant.THRESHOLD_Y):
            screenScroll[1] = (
                gameConstant.SCREEN_HEIGHT - gameConstant.THRESHOLD_Y - self.rect.bottom
            )
            self.rect.bottom = gameConstant.SCREEN_HEIGHT - gameConstant.THRESHOLD_Y

        if self.rect.top < gameConstant.THRESHOLD_Y:
            screenScroll[1] = gameConstant.THRESHOLD_Y - self.rect.top
            self.rect.top = gameConstant.THRESHOLD_Y

        return screenScroll

    def render(self, surface, color):
        flipImage = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(
            flipImage, (self.rect.x, self.rect.y - self.offSet * gameConstant.SCALE)
        )
        # pygame.draw.rect(surface, color, self.rect, 1)
