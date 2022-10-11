from enum import Enum
from xmlrpc.client import Boolean

class Orientation(Enum):
    North = 1
    South = 2
    West = 3
    East = 4

class Coords:
    x: int
    y: int

    def __init__(self, x: int, y:int) -> None:
        self.x = x
        self.y = y

    def isAdjacentTo(self, coor1) -> Boolean:
        return (self.x == coor1.x and abs(coor1.y - self.y) == 1) \
        or (self.y == coor1.y and abs(coor1.x - self.x) == 1)

    def adjacentCells(self, gridWidth: int, gridHeight: int) -> list:
        adCells = []
        # left
        if self.x > 1:
            adCells.append(Coords(self.x - 1, self.y))
        # right
        if self.x < gridWidth:
            adCells.append(Coords(self.x + 1, self.y))
        # down
        if self.y > 1:
            adCells.append(Coords(self.x, self.y - 1))
        # up
        if self.y < gridHeight:
            adCells.append(Coords(self.x, self.y + 1))
        return adCells


class Percept:
    stench: Boolean
    breeze: Boolean
    glitter: Boolean
    bump: Boolean
    scream: Boolean
    isTerminated: Boolean
    reward: float

    def __init__(self):
        self.stench = False
        self.breeze = False
        self.glitter = False
        self.bump = False
        self.scream = False
        self.isTerminated = False
        self.reward = 0.0

    def show(self):
        print(f'stench: {self.stench}, breeze: {self.breeze}, glitter: {self.glitter}, bump: {self.bump}, scream: {self.scream}, isTerminated: {self.isTerminated}, reward: {self.reward}.')

