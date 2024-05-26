import pygame
from config import gameConstant
from utils.imageUtils import scaleImage
import os

pathImageWeapons = "assets/images/weapons/"


class ImageWeapon:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        imageLists = {}
        for name in os.listdir(pathImageWeapons):
            image = pygame.image.load(pathImageWeapons + "/" + name)
            image = scaleImage(image, gameConstant.SCALE_WEAPONS)
            imageLists[name.split(".")[0]] = image
        self.imageLists = imageLists


imageWeaponInstance = ImageWeapon()
