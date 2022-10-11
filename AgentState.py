import Environment as Env

class AgentState:
    location: Env.Coords
    orientation: Env.Orientation
    hasGold: bool
    hasArrow: bool
    isAlive: bool

    def  __init__(self, location:Env.Coords, orientation:Env.Orientation, hasGold: bool, hasArrow: bool, isAlive: bool):
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

    def useArrow(self):
        self.hasArrow = False

    def applyMoveAction(self, action: Env.Action, gridWidth: int, gridHeight: int):
        match action:
            case Env.Action.Forward:
                self.forward(gridWidth, gridHeight)
            case Env.Action.TurnLeft:
                self.turnLeft()
            case Env.Action.TurnRight:
                self.turnRight()
            case _:
                print("not a move action")

    def applyAction(self, action: Env.Action, gridWidth: int, gridHeight: int):
        if action == Env.Action.Shoot:
            self.useArrow()
        else:
            self.applyMoveAction(action, gridWidth, gridHeight)

    def show(self):
        print(f"location: {self.location}, orientation: {self.orientation}, hasGold: {self.hasGold}, hasArrow: {self.hasArrow}, isAlive: {self.isAlive}")