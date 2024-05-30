from characters.enemies import Enemies
from characters.imageCharacter import imageFacotry
from config.gameConstant import HEALTH


class Skeleton(Enemies):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            imageFacotry.imageLists["skeleton"].playerAnimationList,
            HEALTH,
        )
