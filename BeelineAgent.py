import Agent
import Environment
import random

class BeelineAgent(Agent.Agent):
    gridWidth: int
    gridHeight: int
    safeLocations: set
    goldLocation: Environment.Coords
    beelineActionList: list
    
    def __init__(self, gridWidth = 4, gridHeight = 4, safeLocations = set(), 
    goldLocation = None, beelineActionList = []):
        super(BeelineAgent, self).__init__()
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.safeLocations = safeLocations
        self.goldLocation = goldLocation
        self.beelineActionList = beelineActionList

    def nextAction(self, agentState: Environment.AgentState, percept: Environment.Percept) -> Environment.Action:
        if not agentState.hasGold:
            self.safeLocations.add(agentState.location)

        if agentState.hasGold and agentState.location == Environment.Coords(1,1):
            return Environment.Action.Climb

        if percept.glitter:
            self.goldLocation = agentState.location
            return Environment.Action.Grab

        randAction = random.randint(1, 4)
        if randAction == 1:
            return Environment.Action.Forward
        if randAction == 2:
            return Environment.Action.TurnLeft
        if randAction == 3:
            return Environment.Action.TurnRight
        if randAction == 4:
            return Environment.Action.Shoot

    def _bfs_shortestpath(self) -> list:
        path = []
        explored = []
        visited = []
        path_dict = {}
        desti = Environment.Coords(1,1)
        start = self.goldLocation
        explored.append(start)
        curr = explored.pop(0)
        visited.append(curr)
        while curr != desti:
            for coord in self._adjacent(curr, 4, 4):
                if coord in self.safeLocations and (not coord in visited):
                    explored.append(coord)
                    path_dict.update({coord:curr})
                    visited.append(coord)
            curr = explored.pop(0)
            if curr == desti:
                path_dict.update({desti:curr})
        
        path.append(desti)
        prev_path = path_dict.get(desti)
        path.insert(0,prev_path)
        while prev_path != start:
            prev_path = path_dict.get(prev_path)
            path.insert(0,prev_path)
        return path
            

    def _adjacent(coords: Environment.Coords, gridW: int, gridH:int) -> list:
        return [
            Environment.Coords(coords.x - 1, coords.y) if coords.x > 1 else None, # to left
            Environment.Coords(coords.x + 1, coords.y) if coords.x < gridW else None, # to right
            Environment.Coords(coords.x, coords.y - 1) if coords.y > 1 else None, # to down
            Environment.Coords(coords.x, coords.y + 1) if coords.y < gridH else None # to up
        ]






