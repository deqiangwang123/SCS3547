from enum import Enum
import copy
import random
from collections import namedtuple

class Orientation(Enum):
    North = 1
    South = 2
    West = 3
    East = 4

    @property
    def turn_left(self):
        dict_turn_left = {
            Orientation.North: Orientation.West,
            Orientation.West: Orientation.South,
            Orientation.South: Orientation.East,
            Orientation.East: Orientation.North
        }
        new_orientation = dict_turn_left.get(self)
        return new_orientation

    @property
    def turn_right(self):
        dict_turn_right = {
            Orientation.North: Orientation.East,
            Orientation.East: Orientation.South,
            Orientation.South: Orientation.West,
            Orientation.West: Orientation.North
        }
        new_orientation = dict_turn_right.get(self)
        return new_orientation

class Action(Enum):
    Forward = 1
    TurnLeft = 2
    TurnRight = 3
    Shoot = 4
    Grab = 5
    Climb = 6

class Coords(namedtuple('Coords', 'x y')):
    pass


# class Coords:
#     x: int
#     y: int

#     def __init__(self, x: int, y:int) -> None:
#         self.x = x
#         self.y = y

#     def isAdjacentTo(self, coor1) -> bool:
#         return (self.x == coor1.x and abs(coor1.y - self.y) == 1) \
#         or (self.y == coor1.y and abs(coor1.x - self.x) == 1)

#     def adjacentCells(self, gridWidth: int, gridHeight: int) -> list:
#         adCells = []
#         # left
#         if self.x > 1:
#             adCells.append(Coords(self.x - 1, self.y))
#         # right
#         if self.x < gridWidth:
#             adCells.append(Coords(self.x + 1, self.y))
#         # down
#         if self.y > 1:
#             adCells.append(Coords(self.x, self.y - 1))
#         # up
#         if self.y < gridHeight:
#             adCells.append(Coords(self.x, self.y + 1))
#         return adCells

#     def isEqual(self, coor1) -> bool:
#         return (self.x == coor1.x) and (self.y == coor1.y)

#     def isInside(self, coors: list) -> bool:
#         coors_xy = []
#         for coor in coors:
#             coors_xy.append((coor.x, coor.y))
#         return (self.x, self.y) in set(coors_xy)

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

    def  __init__(self, location: Coords = Coords(1,1), orientation:Orientation = Orientation.East, hasGold: bool =False, hasArrow: bool = True, isAlive: bool = True):
        self.location = location
        self.orientation = orientation
        self.hasGold = hasGold
        self.hasArrow = hasArrow
        self.isAlive = isAlive

    def turnLeft(self):
        new_state = copy.deepcopy(self)
        new_state.orientation = new_state.orientation.turn_left
        return new_state

    def turnRight(self):
        new_state = copy.deepcopy(self)
        new_state.orientation = new_state.orientation.turn_right
        return new_state

    def forward(self, gridWidth: int, gridHeight: int):
        if self.orientation == Orientation.North:
            new_loc = Coords(self.location.x, min(gridHeight, self.location.y + 1))
        elif self.orientation == Orientation.South:
            new_loc = Coords(self.location.x, max(1, self.location.y - 1))
        elif self.orientation == Orientation.West:
            new_loc = Coords(max(self.location.x - 1, 1), self.location.y)
        elif self.orientation == Orientation.East:
            new_loc = Coords(min(self.location.x + 1, gridWidth), self.location.y)           
        new_state = copy.deepcopy(self)
        new_state.location = new_loc
        return new_state

    # def useArrow(self):
    #     self.hasArrow = False

    # def applyMoveAction(self, action: Action, gridWidth: int, gridHeight: int):
    #     if action == Action.Forward:
    #         self.forward(gridWidth, gridHeight)
    #     elif action == Action.TurnLeft:
    #         self.turnLeft()
    #     elif action == Action.TurnRight:
    #         self.turnRight()

    # def applyAction(self, action: Action, gridWidth: int, gridHeight: int):
    #     if action == Action.Shoot:
    #         self.useArrow()
    #     else:
    #         self.applyMoveAction(action, gridWidth, gridHeight)

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

    def __init__(self, grid_width, grid_height, pit_prob, allow_climb_without_gold, agent, pit_locations,
                 terminated, wumpus_loc, wumpus_alive, gold_loc) -> None:
        self.gridWidth = grid_width
        self.gridHeight = grid_height
        self.pitProb = pit_prob
        self.allowClimbWithoutGold = allow_climb_without_gold
        self.agent = agent
        self.pitLocations = pit_locations
        self.terminated = terminated
        self.wumpusLocation = wumpus_loc
        self.wumpusAlive = wumpus_alive
        self.goldLocation = gold_loc
        self.percept = Percept()

    def _isPitAt(self, coords: Coords) -> bool:
        return coords in self.pitLocations

    def _isWumpusAt(self, coords: Coords) -> bool:
        return coords == self.wumpusLocation

    def _isAgentAt(self, coords: Coords) -> bool:
        return coords == self.agent.location

    def _isGlitter(self) -> bool:
        return self.goldLocation == self.agent.location

    def _isGoldAt(self, coords: Coords) -> bool:
        return coords == self.goldLocation    

    def _wumpusInLineOfFire(self) -> bool:
        if self.agent.orientation == Orientation.West:
            return (self.agent.location.x > self.wumpusLocation.x) and (self.agent.location.y == self.wumpusLocation.y)
        elif self.agent.orientation == Orientation.East:
            return (self.agent.location.x < self.wumpusLocation.x) and (self.agent.location.y == self.wumpusLocation.y)
        elif self.agent.orientation == Orientation.North:
            return (self.agent.location.x == self.wumpusLocation.x) and (self.agent.location.y < self.wumpusLocation.y)
        elif self.agent.orientation == Orientation.South:
            return (self.agent.location.x == self.wumpusLocation.x) and (self.agent.location.y > self.wumpusLocation.y)           

    def _killAttemptSuccessful(self) -> bool:
        return self.agent.hasArrow and self.wumpusAlive and self._wumpusInLineOfFire()

    def _adjacentCells(self, coords: Coords = Coords(1,1)) ->list:
        return [
            Coords(coords.x - 1, coords.y) if coords.x > 1 else None, # to left
            Coords(coords.x + 1, coords.y) if coords.x < self.gridWidth else None, # to right
            Coords(coords.x, coords.y - 1) if coords.y > 1 else None, # to down
            Coords(coords.x, coords.y + 1) if coords.y < self.gridHeight else None # to up
        ]

    def _isPitAdjacent(self, coords: Coords = Coords(1, 1)) -> bool:
        for pit in self.pitLocations:
            if pit.isInside(coords.adjacentCells(self.gridWidth, self.gridHeight)):
                return True
        return False     

    def _isWumpusAdjacent(self, coords: Coords) -> bool:
        return self.wumpusLocation.isInside(coords.adjacentCells(self.gridWidth, self.gridHeight))

    def _isBreeze(self) -> bool:
        return self._isPitAdjacent(self.agent.location)

    def _isStench(self) -> bool:
        return self._isWumpusAdjacent(self.agent.location) or self._isWumpusAt(self.agent.location)    

    def _get_random_location(self, gridWidth: int, gridHeight: int) -> Coords:
        """ _get_random_location: return a random location that is not the (1,1) square """
        locations = []
        for x in range(1, gridWidth + 1):
            for y in range(1, gridHeight + 1):
                locations.append(Coords(x = x,y = y))
        locations.remove(Coords(1,1))
        return random.choice(locations)

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
                if (x != 1) and (y != 1):
                    # Using the PIT_PROBABILITY, randomly determine if a pit will be at this location
                    if random.random() < self.pitProb:
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
                isbump : bool = True if prev_loc.isEqual(self.agent.location) else False
                # update percept
                self.percept.setPercept(stench=self._isStench(), breeze=self._isBreeze(), glitter=self._isGlitter(), bump=isbump, \
                    scream= False, isTerminated= not self.agent.isAlive, reward = -1 if self.agent.isAlive else -1001)
            if action == Action.TurnLeft:
                # update agent state
                self.agent.turnLeft()
                # update percept
                self.percept.setPercept(stench=self._isStench(), breeze=self._isBreeze(), glitter=self._isGlitter(), bump=False, \
                    scream= False, isTerminated= False, reward = -1)  
            if action == Action.TurnRight:
                # update agent state
                self.agent.turnRight()
                # update percept
                self.percept.setPercept(stench=self._isStench(), breeze=self._isBreeze(), glitter=self._isGlitter(), bump=False, \
                    scream= False, isTerminated= False, reward = -1)  
            if action == Action.Grab:
                # update has gold
                self.agent.hasGold = self._isGlitter()
                # update gold location
                if self.agent.hasGold:
                    self.goldLocation = self.agent.location
                # update percept               
                self.percept.setPercept(stench=self._isStench(), breeze=self._isBreeze(), glitter=self._isGlitter(), bump=False, \
                    scream= False, isTerminated= False, reward = -1)  

            if action == Action.Climb:
                inStartLocation: bool = ((self.agent.location.x == 1) and (self.agent.location.y == 1))
                success: bool = self.agent.hasGold and inStartLocation
                isTerminated: bool = success or (self.allowClimbWithoutGold and inStartLocation)
                # update environment
                self.terminated = isTerminated
                # update percept
                if isTerminated:
                    self.percept.setPercept(stench=False, breeze=False, glitter=self._isGlitter(), bump=False, \
                        scream= False, isTerminated= isTerminated, reward = 999 if success else -1)
                else:
                    self.percept.setPercept(stench=self._isStench(), breeze=self._isBreeze(), glitter=self._isGlitter(), bump=False, \
                        scream= False, isTerminated= False, reward = -1)
            if action == Action.Shoot:                        
                hasArrow: bool = self.agent.hasArrow
                wumpusKilled: bool = self._killAttemptSuccessful()
                # update environment
                self.agent.hasArrow = False
                self.wumpusAlive = self.wumpusAlive and not wumpusKilled
                # update percept
                self.percept.setPercept(stench=self._isStench(), breeze=self._isBreeze(), glitter=self._isGlitter(), bump=False, \
                    scream= wumpusKilled, isTerminated= False, reward = -11 if hasArrow else -1)
            
    def visualize(self) -> str:
        st:list = []
        for y in range(self.gridHeight, 0, -1):
            # for x in range(self.gridWidth, 0, -1):
            for x in range(1, self.gridWidth+1):
                st.append(self.gridSymbol(x,y))
                if x != 4:
                    st.append("|")
            st.append("\n")   
        return "".join(st)

    def gridSymbol(self, x:int, y:int) -> str:
        wumpusSymbol = 'W ' if self.wumpusAlive else 'w '
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
            return "P "
        elif self._isGoldAt(Coords(x, y)):
            return "G "
        elif self._isWumpusAt(Coords(x, y)):
            return wumpusSymbol
        else:
            return "  "