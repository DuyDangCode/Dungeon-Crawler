from characters.baseCharacter import BaseCharacter
from characters.imageCharacter import imageFacotry
from config import charactersConstant
from config.gameConstant import HEALTH


class Skeleton(BaseCharacter):
    def __init__(self, x, y):
        super().__init__(
            x,
            y,
            imageFacotry.imageLists[
                charactersConstant.skeletonName
            ].playerAnimationList,
            HEALTH,
        )
