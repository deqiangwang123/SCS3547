import BeelineAgent
import PitLocationProb
import WumpusLocationProb
import Environment
import random

class ProbAgent(BeelineAgent.BeelineAgent):
	def __init__(self, gridWidth = 4, gridHeight = 4, safeLocations = set(), goldLocation = None, shortestPath = [], beelineActionList = []):
		super(ProbAgent, self).__init__(gridWidth, gridHeight, safeLocations, goldLocation, shortestPath, beelineActionList)
    
	def nextAction(self, agentState: Environment.AgentState, percept: Environment.Percept) -> Environment.Action:
		if not agentState.hasGold:
			self.safeLocations.add(agentState.location)

		if agentState.hasGold and agentState.location == Environment.Coords(1,1):
			return Environment.Action.Climb

		if percept.glitter and not agentState.hasGold:
			self.goldLocation = agentState.location
			self.shortestPath = self._bfs_shortestpath()
			return Environment.Action.Grab

		if agentState.hasGold:
			if agentState.orientation != self._requireOrientation():
				return self._turn(agentState.orientation, self._requireOrientation())
			else:
				self.shortestPath.pop(0)
				return Environment.Action.Forward

		randAction = random.randint(1, 4)
		if randAction == 1:
			return Environment.Action.Forward
		if randAction == 2:
			return Environment.Action.TurnLeft
		if randAction == 3:
			return Environment.Action.TurnRight
		if randAction == 4:
			return Environment.Action.Shoot                


if __name__ == '__main__':
	probAgent =  ProbAgent()
	print(1)
