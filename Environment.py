from enum import Enum
from AgentState import AgentState


class Orientation(Enum):
    North = 1
    South = 2
    West = 3
    East = 4

class Action(Enum):
    Forward = 1
    TurnLeft = 2
    TurnRight = 3
    Shoot = 4
    Grab = 5
    Climb = 6

class Coords:
    x: int
    y: int

    def __init__(self, x: int, y:int) -> None:
        self.x = x
        self.y = y

    def isAdjacentTo(self, coor1) -> bool:
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
    stench: bool
    breeze: bool
    glitter: bool
    bump: bool
    scream: bool
    isTerminated: bool
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

class Environment:
    gridWidth: int
    gridHeight: int
    pitProb: int
    allowClimbWithoutGold: bool
    agent: AgentState
    pitLocations: list[Coords]
    terminated: bool
    wumpusLocation: Coords
    wumpusAlive: bool
    goldLocation: Coords
    percept: Percept = Percept()

    def __init__(self, gridWidth: int, gridHeight: int, pitProb: int, allowClimbWithoutGold: bool,\
        agent: AgentState, terminated: bool, wumpusAlive: bool) -> None:
        pass

    def _isPitAt(self, coords: Coords) -> bool:
        if coords in self.pitLocations:
            return True
        else:
            return False

    def _isWumpusAt(self, coords: Coords) -> bool:
        if coords == self.wumpusLocation:
            return True
        else:
            return False

    def _isAgentAt(self, coords: Coords) -> bool:
        if coords == self.agent.location:
            return True
        else:
            return False

    def _isGlitter(self) -> bool:
        if self.goldLocation == self.agent.location:
            return True
        else:
            return False

    def _isGoldAt(self, coords: Coords) -> bool:
        if coords == self.goldLocation:
            return True
        else:
            return False            

    def _wumpusInLineOfFire(self) -> bool:
        match self.agent.orientation:
            case Orientation.West:
                return (self.agent.location.x > self.wumpusLocation.x) and (self.agent.location.y == self.wumpusLocation.y)
            case Orientation.East:
                return (self.agent.location.x < self.wumpusLocation.x) and (self.agent.location.y == self.wumpusLocation.y)
            case Orientation.North:
                return (self.agent.location.x == self.wumpusLocation.x) and (self.agent.location.y < self.wumpusLocation.y)
            case Orientation.North:
                return (self.agent.location.x == self.wumpusLocation.x) and (self.agent.location.y > self.wumpusLocation.y)
            case _:
                print("no agent orientation")
                return False

    def _killAttemptSuccessful(self) -> bool:
        if self.agent.hasArrow and self.wumpusAlive and self._wumpusInLineOfFire():
            return True
        else:
            return False

    def _isPitAdjacent(self, coords: Coords) -> bool:
        if set(Coords.adjacentCells()) & set(self.pitLocations):
            return True
        else:
            return False      

    def _isWumpusAdjacent(self, coords: Coords) -> bool:
        if self.wumpusLocation in Coords.adjacentCells():
            return True
        else:
            return False

    def _isBreeze(self, coords: Coords) -> bool:
        if self._isPitAdjacent(self.agent.location):
            return True
        else:
            return False

    def _isStench(self, coords: Coords) -> bool:
        if self._isWumpusAdjacent(self.agent.location) or self._isWumpusAt(self.agent.location):
            return True
        else:
            return False        

    def applyAction(self):
        if self.terminated:
            self.percept.isTerminated = True
            