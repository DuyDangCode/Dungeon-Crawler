import os

import pygame

from utils.imageUtils import scaleImage
from config import gameConstant

pathImageTile = "assets/images/tiles"


class ImageTile:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.imageList = {}
        for i in os.listdir(pathImageTile):
            self.imageList[i.split(".")[0]] = scaleImage(
                pygame.image.load(pathImageTile + "/" + i), gameConstant.SCALE
            )


imageTileInstance = ImageTile()
