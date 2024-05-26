import os

import pygame

from utils.imageUtils import scaleImage
from config import gameConstant


pathImageItem = "assets/images/items"


class ImageItem:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self):
        self.imagesList = {}
        for image in os.listdir(pathImageItem):
            self.imagesList[image.split(".")[0]] = scaleImage(
                pygame.image.load(pathImageItem + "/" + image), gameConstant.SCALE_ITEMS
            )


imageItemInstance = ImageItem()
