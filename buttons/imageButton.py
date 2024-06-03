import os

import pygame

from utils.imageUtils import scaleImage
from config.gameConstant import SCALE


path = "assets/images/buttons"


class ButtonImage:
    def __new__(cls):
        if not hasattr(cls, "instance"):
            cls.instance = super().__new__(cls)
        return cls.instance

    def __init__(self) -> None:
        self.imagesList = {}
        for imageName in os.listdir(path):
            self.imagesList[imageName.split(".")[0]] = scaleImage(
                pygame.image.load(path + "/" + imageName), 1
            )


buttonImage = ButtonImage()
