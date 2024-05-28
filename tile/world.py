import os
from tile.imageTile import imageTileInstance
from config import gameConstant
import csv

pathLevel = "levels"


class World:
    def __init__(self):
        self.maps = {}
        for level in os.listdir(pathLevel):
            self.maps[str(level.split(".")[0])] = []
        for level in os.listdir(pathLevel):
            with open(f"{pathLevel}/{level}", newline="") as csvFile:
                reader = csv.reader(csvFile, delimiter=",")
                for row in reader:
                    data = []
                    for tile in row:
                        data.append(int(tile))
                    self.maps[str(level).split(".")[0]].append(data)

    def render(self, surface, level=1):
        for y, row in enumerate(self.maps[str(level)]):
            for x, tileId in enumerate(row):
                if tileId == -1:
                    continue
                surface.blit(
                    imageTileInstance.imageList[str(tileId)],
                    (
                        x * gameConstant.TILE_SIZE,
                        y * gameConstant.TILE_SIZE,
                    ),
                )
