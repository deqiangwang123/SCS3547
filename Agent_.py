import Environ as Env

class Agent:
    location: Env.Coords
    orientation: Env.Orientation
    hasGold: bool
    hasArrow: bool
    isAlive: bool

    def  __init__(self, location:Env.Coords, orientation:Env.Orientation, hasGold: bool, hasArrow: bool, isAlive: bool):
        self.location = location
        self.orientation = orientation
        self.hasGold = False
        self.hasArrow = True
        self.isAlive = False

    def turnLeft(self):
        if self.orientation == Env.Orientation.North:
            self.orientation = Env.Orientation.West
        if self.orientation == Env.Orientation.South:
            self.orientation = Env.Orientation.East
        if self.orientation == Env.Orientation.West:
            self.orientation = Env.Orientation.South
        if self.orientation == Env.Orientation.East:
            self.orientation = Env.Orientation.North

    def turnRight(self):
        if self.orientation == Env.Orientation.North:
            self.orientation = Env.Orientation.East
        if self.orientation == Env.Orientation.South:
            self.orientation = Env.Orientation.West
        if self.orientation == Env.Orientation.West:
            self.orientation = Env.Orientation.North
        if self.orientation == Env.Orientation.East:
            self.orientation = Env.Orientation.South

    def forward(self, gridWidth: int, gridHeight: int):
        if self.orientation == Env.Orientation.North:
            self.location = Env.Coords(self.x, min(gridHeight, self.y + 1))
        if self.orientation == Env.Orientation.South:
            self.location = Env.Coords(self.x, max(1, self.y - 1))
        if self.orientation == Env.Orientation.West:
            self.location = Env.Coords(max(self.x - 1, 1), self.y)
        if self.orientation == Env.Orientation.East:
            self.location = Env.Coords(min(self.x + 1, gridWidth), self.y)    