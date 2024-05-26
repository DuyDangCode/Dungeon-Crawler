import pygame
from characters.baseCharacter import BaseCharacter
from characters.imageCharacter import imageFacotry
from config import gameConstant, charactersConstant
from weapons.arrow import Arrow


class Elf(BaseCharacter):
    def __init__(self, x, y):
        self.offSet = 12
        super().__init__(
            x,
            y,
            imageFacotry.imageLists[charactersConstant.elfName].playerAnimationList,
            60,
        )

    def render(self, surface, color):
        flipImage = pygame.transform.flip(self.image, self.flip, False)
        surface.blit(
            flipImage, (self.rect.x, self.rect.y - self.offSet * gameConstant.SCALE)
        )
        pygame.draw.rect(surface, color, self.rect, 1)
