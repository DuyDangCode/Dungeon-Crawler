import pygame

from item.imageItem import imageItemInstance


class Heart:
    def __init__(self, player) -> None:
        self.player = player

    def render(self, surface):
        drawHalfHeart = False
        for i in range(5):
            if self.player.health >= (i + 1) * 20:
                surface.blit(
                    imageItemInstance.imagesList["heart_full"], (10 + i * 50, 0)
                )
            elif self.player.health % ((i + 1) * 20) > 0 and not drawHalfHeart:
                surface.blit(
                    imageItemInstance.imagesList["heart_half"], (10 + i * 50, 0)
                )
                drawHalfHeart = True
            else:
                surface.blit(
                    imageItemInstance.imagesList["heart_empty"], (10 + i * 50, 0)
                )
