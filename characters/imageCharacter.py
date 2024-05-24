import pygame
from config import gameConstant
from utils.imageUtils import scaleImage
import os

pathPlayerImage = "assets/images/characters/"


class BaseImage:
    def __init__(self, path):
        playerAnimationList = []
        for a in os.listdir(path):
            animationTemp = []
            for i in os.listdir(path + "/" + a):
                playerImage = pygame.image.load(path + "/" + a + "/" + i)
                playerImage = scaleImage(playerImage, gameConstant.SCALE)
                animationTemp.append(playerImage)
            playerAnimationList.append(animationTemp)

        self.playerAnimationList = playerAnimationList


class ImageFactory:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        imageLists = {}
        for name in os.listdir(pathPlayerImage):
            imageLists[name] = BaseImage(pathPlayerImage + name)
        self.imageLists = imageLists


imageFacotry = ImageFactory()
