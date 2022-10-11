from xmlrpc.client import Boolean
import Environment as Env

class Agent:
    location: Env.Coords
    orientation: Env.Orientation
    hasGold: Boolean
    hasArrow: Boolean
    isAlive: Boolean

    def  __init__(self, location:Env.Coords, orientation:Env.Orientation, hasGold: Boolean, hasArrow: Boolean, isAlive: Boolean):
        self.location = Env.Coords(1, 1)
        self.orientation = Env.Orientation.East
        self.hasGold = False
        self.hasArrow = True
        self.isAlive = False

    def turnLeft(self):
        match self.orientation:
            case Env.Orientation.North:
                self.orientation = Env.Orientation.West
            case Env.Orientation.South:
                self.orientation = Env.Orientation.East
            case Env.Orientation.West:
                self.orientation = Env.Orientation.South
            case Env.Orientation.East:
                self.orientation = Env.Orientation.North
            case _:
                print("turn left error")

    def turnRight(self):
        match self.orientation:
            case Env.Orientation.North:
                self.orientation = Env.Orientation.East
            case Env.Orientation.South:
                self.orientation = Env.Orientation.West
            case Env.Orientation.West:
                self.orientation = Env.Orientation.North
            case Env.Orientation.East:
                self.orientation = Env.Orientation.South
            case _:
                print("turn right error")

    def forward(self, gridWidth: int, gridHeight: int):
        match self.orientation:
            case Env.Orientation.North:
                self.location = Env.Coords(self.x, min(gridHeight, self.y + 1))
            case Env.Orientation.South:
                self.location = Env.Coords(self.x, max(1, self.y - 1))
            case Env.Orientation.West:
                self.location = Env.Coords(max(self.x - 1, 1), self.y)
            case Env.Orientation.East:
                self.location = Env.Coords(min(self.x + 1, gridWidth), self.y)
            case _:
                print("forward error")