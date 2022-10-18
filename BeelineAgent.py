import Agent
import Environment
import random

class BeelineAgent(Agent.Agent):
    gridWidth: int
    gridHeight: int
    safeLocations: set
    beelineActionList: list
    
    def __init__(self, gridWidth = 4, gridHeight = 4, safeLocations = None, 
    beelineActionList = None):
        super(BeelineAgent, self).__init__()
        self.gridWidth = gridWidth
        self.gridHeight = gridHeight
        self.safeLocations = safeLocations
        self.beelineActionList = beelineActionList

    def nextAction(self, agentState: Environment.AgentState, percept: Environment.Percept) -> Environment.Action:
        if not agentState.hasGold:
            self.safeLocations.add(agentState.location)

        if agentState.hasGold and agentState.location == Environment.Coords(1,1):
            return Environment.Action.Climb

        if percept.glitter:
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



