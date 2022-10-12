from enum import Enum
# from Agent_State import AgentState
# from Agent_State import *
import random

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

    def isEqual(self, coor1) -> bool:
        if (self.x == coor1.x) and (self.y == coor1.y):
            return True
        else:
            return False

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

    def setPercept(self, stench: bool, breeze: bool, glitter: bool, bump: bool, scream: bool, isTerminated: bool, reward: float):
        self.stench = stench
        self.breeze = breeze
        self.glitter = glitter
        self.bump = bump
        self.scream = scream
        self.isTerminated = isTerminated
        self.reward = reward

class AgentState:
    location: Coords
    orientation: Orientation
    hasGold: bool
    hasArrow: bool
    isAlive: bool

    def  __init__(self, location:Coords, orientation:Orientation, hasGold: bool, hasArrow: bool, isAlive: bool):
        self.location = location
        self.orientation = orientation
        self.hasGold = hasGold
        self.hasArrow = hasArrow
        self.isAlive = isAlive

    def turnLeft(self):
        if self.orientation == Orientation.North:
            self.orientation = Orientation.West
        if self.orientation == Orientation.South:
            self.orientation = Orientation.East
        if self.orientation == Orientation.West:
            self.orientation = Orientation.South
        if self.orientation == Orientation.East:
            self.orientation = Orientation.North

    def turnRight(self):
        if self.orientation == Orientation.North:
            self.orientation = Orientation.East
        if self.orientation == Orientation.South:
            self.orientation = Orientation.West
        if self.orientation == Orientation.West:
            self.orientation = Orientation.North
        if self.orientation == Orientation.East:
            self.orientation = Orientation.South

    def forward(self, gridWidth: int, gridHeight: int):
        if self.orientation == Orientation.North:
            self.location = Coords(self.location.x, min(gridHeight, self.location.y + 1))
        if self.orientation == Orientation.South:
            self.location = Coords(self.location.x, max(1, self.location.y - 1))
        if self.orientation == Orientation.West:
            self.location = Coords(max(self.location.x - 1, 1), self.location.y)
        if self.orientation == Orientation.East:
            self.location = Coords(min(self.location.x + 1, gridWidth), self.location.y)    

    def useArrow(self):
        self.hasArrow = False

    def applyMoveAction(self, action: Action, gridWidth: int, gridHeight: int):
        if action == Action.Forward:
            self.forward(gridWidth, gridHeight)
        if action == Action.TurnLeft:
            self.turnLeft()
        if action == Action.TurnRight:
            self.turnRight()

    def applyAction(self, action: Action, gridWidth: int, gridHeight: int):
        if action == Action.Shoot:
            self.useArrow()
        else:
            self.applyMoveAction(action, gridWidth, gridHeight)

    def show(self):
        print(f"location: {self.location}, orientation: {self.orientation}, hasGold: {self.hasGold}, hasArrow: {self.hasArrow}, isAlive: {self.isAlive}")


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
    percept: Percept

    def __init__(self, gridWidth: int, gridHeight: int, pitProb: int, allowClimbWithoutGold: bool) -> None:
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.pitProb = pitProb
        self.allowClimbWithoutGold = allowClimbWithoutGold
        self.agent = AgentState(location=Coords(1,1), orientation=Orientation.East, hasGold=False, hasArrow=True, isAlive=True)
        self.pitLocations = self._get_pit_locations(gridWidth, gridHeight)
        self.terminated = False
        self.wumpusLocation = self._get_wumpus_location()
        self.wumpusAlive = True
        self.goldLocation = self._get_gold_location()
        self.percept = Percept()

    def _isPitAt(self, coords: Coords) -> bool:
        # pitSet:set = set(list[(x, y) for ])
        if coords in self.pitLocations:
            return True
        else:
            return False

    def _isWumpusAt(self, coords: Coords) -> bool:
        if coords.isEqual(self.wumpusLocation):
            return True
        else:
            return False

    def _isAgentAt(self, coords: Coords) -> bool:
        if coords.isEqual(self.agent.location):
            return True
        else:
            return False

    def _isGlitter(self) -> bool:
        if self.goldLocation.isEqual(self.agent.location):
            return True
        else:
            return False

    def _isGoldAt(self, coords: Coords) -> bool:
        if coords.isEqual(self.goldLocation):
            return True
        else:
            return False            

    def _wumpusInLineOfFire(self) -> bool:
        if self.agent.orientation == Orientation.West:
            return (self.agent.location.x > self.wumpusLocation.x) and (self.agent.location.y == self.wumpusLocation.y)
        if self.agent.orientation == Orientation.East:
            return (self.agent.location.x < self.wumpusLocation.x) and (self.agent.location.y == self.wumpusLocation.y)
        if self.agent.orientation == Orientation.North:
            return (self.agent.location.x == self.wumpusLocation.x) and (self.agent.location.y < self.wumpusLocation.y)
        if self.agent.orientation == Orientation.South:
            return (self.agent.location.x == self.wumpusLocation.x) and (self.agent.location.y > self.wumpusLocation.y)           

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

    def _get_random_location(self, gridWidth: int, gridHeight: int) -> Coords:
        """ _get_random_location: return a random location that is not the (1,1) square """
        x = 1
        y = 1

        while (x == 1) and (y == 1):
            x = random.randint(1, gridWidth)
            y = random.randint(1, gridHeight)

        return Coords(x, y)

    def _get_gold_location(self) -> Coords:
        """ _get_gold_location: return a random location not (1,1) for the gold's location """
        return self._get_random_location(self.gridWidth, self.gridHeight)

    def _get_wumpus_location(self) -> Coords:
        """ _get_wumpus_location: return a random location, not (1,1) for the wumpus's location """
        return self._get_random_location(self.gridWidth, self.gridHeight)

    def _get_pit_locations(self, gridWidth: int, gridHeight: int):
        """ _get_pit_locations: returns an array of pit locations, randomly selected based on a probability """
        locations = []
        for x in range(1, gridWidth + 1):
            for y in range(1, gridHeight + 1):
                if (x != 1) or (y != 1):
                    # Using the PIT_PROBABILITY, randomly determine if a pit will be at this location
                    if (random.randint(0, 1000 - 1)) < (0.2 * 1000):
                        locations.append(Coords(x, y))
        return locations

    def applyAction(self, action: Action):
        if self.terminated:
            self.percept.setPercept(stench=False, breeze=False, glitter=False, bump=False, scream=False, isTerminated=True, reward=0)
        else:
            if action == Action.Forward:
                # move agent
                prev_loc : Coords = self.agent.location
                self.agent.forward(self.gridWidth, self.gridHeight)
                # death
                death : bool = (self._isWumpusAt(self.agent.location) and self.wumpusAlive) or self._isPitAt(self.agent.location)
                # update agent state
                self.agent.isAlive = not death
                # update environment state
                self.terminated = death
                if self.agent.hasGold:
                    self.goldLocation = self.agent.location
                # update bump
                isbump : bool = True if prev_loc == self.agent.location else False
                # update percept
                self.percept.setPercept(stench=self._isStench, breeze=self._isBreeze, glitter=self._isGlitter, bump=isbump, \
                    scream= False, isTerminated= not self.agent.isAlive, reward = -1 if self.agent.isAlive else -1001)
            if action == Action.TurnLeft:
                # update agent state
                self.agent.turnLeft()
                # update percept
                self.percept.setPercept(stench=self._isStench, breeze=self._isBreeze, glitter=self._isGlitter, bump=False, \
                    scream= False, isTerminated= False, reward = -1)  
            if action == Action.TurnRight:
                # update agent state
                self.agent.turnRight()
                # update percept
                self.percept.setPercept(stench=self._isStench, breeze=self._isBreeze, glitter=self._isGlitter, bump=False, \
                    scream= False, isTerminated= False, reward = -1)  
            if action == Action.Grab:
                # update has gold
                self.agent.hasGold = self._isGlitter()
                # update gold location
                if self.agent.hasGold:
                    self.goldLocation = self.agent.location
                # update percept
                if self.agent.hasGold:
                    self.percept.setPercept(stench=self._isStench, breeze=self._isBreeze, glitter=self._isGlitter, bump=False, \
                        scream= False, isTerminated= False, reward = -1)  
            if action == Action.Climb:
                inStartLocation: bool = ((self.agent.location.x == 1) and (self.agent.location.y == 1))
                success: bool = self.agent.hasGold and inStartLocation
                isTerminated: bool = success or (self.allowClimbWithoutGold and inStartLocation)
                # update environment
                self.terminated = isTerminated
                # update percept
                if isTerminated:
                    self.percept.setPercept(stench=False, breeze=False, glitter=self._isGlitter, bump=False, \
                        scream= False, isTerminated= isTerminated, reward = 999 if success else -1)
                else:
                    self.percept.setPercept(stench=self._isStench, breeze=self._isBreeze, glitter=self._isGlitter, bump=False, \
                        scream= False, isTerminated= False, reward = -1)
            if action == Action.Shoot:                        
                hasArrow: bool = self.agent.hasArrow
                wumpusKilled: bool = self._killAttemptSuccessful()
                # update environment
                self.agent.hasArrow = False
                self.wumpusAlive = self.wumpusAlive and not wumpusKilled
                # update percept
                self.percept.setPercept(stench=self._isStench, breeze=self._isBreeze, glitter=self._isGlitter, bump=False, \
                    scream= wumpusKilled, isTerminated= False, reward = -11 if hasArrow else -1)
            
    def visualize(self) -> str:
        st:list = []
        for y in range(self.gridHeight, 0, -1):
            # for x in range(self.gridWidth, 0, -1):
            for x in range(1, self.gridWidth+1):
                st.append(self.gridSymbol(x,y))
                if x != 1:
                    st.append("|")
            st.append("\n")   
        return "".join(st)

    def gridSymbol(self, x:int, y:int) -> str:
        wumpusSymbol = 'W' if self.wumpusAlive else 'w'
        if self._isAgentAt(Coords(x, y)):
            if self.agent.orientation == Orientation.West:
                return "A<"
            if self.agent.orientation == Orientation.East:
                return "A>"
            if self.agent.orientation == Orientation.North:               
                return "A^"
            if self.agent.orientation == Orientation.South:  
                return "Av"                    
        elif self._isPitAt(Coords(x, y)):
            return "P"
        elif self._isGoldAt(Coords(x, y)):
            return "G"
        elif self._isWumpusAt(Coords(x, y)):
            return wumpusSymbol
        else:
            return " "
        


