import pygame
from config import gameConstant
from utils.imageUtils import scaleImage
import os

pathPlayerImage = "assets/images/weapons/"


class ImageWeapon:
    def __new__(cls, arg):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self, path) -> None:
        imageLists = {}
        for name in os.listdir(path):
            image = pygame.image.load(path + "/" + name)
            image = scaleImage(image, gameConstant.SCALE_WEAPONS)
            imageLists[name.split(".")[0]] = image
        self.imageLists = imageLists
        print(self.imageLists.keys())


imageWeaponInstance = ImageWeapon(pathPlayerImage)
