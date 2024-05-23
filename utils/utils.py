import pygame


def scaleImage(image, scale):
    return pygame.transform.scale(
        image, (image.get_width() * scale, image.get_height() * scale)
    )
