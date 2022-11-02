from heapq import heappush,heappop
from pyrsistent import s
import BeelineAgent
import PitLocationProb
import WumpusLocationProb
import Environment
import random
import numpy as np

class ProbAgent(BeelineAgent.BeelineAgent):
	wumpusLocProb: 	WumpusLocationProb.WumpusLocationProb
	pitLocProb: 	PitLocationProb.PitLocationProb
	riskProb: 		np.ndarray
	unexploredQueue: list

	def __init__(self, gridWidth = 4, gridHeight = 4, safeLocations = set(), goldLocation = None, shortestPath = [], beelineActionList = []):
		super(ProbAgent, self).__init__(gridWidth, gridHeight, safeLocations, goldLocation, shortestPath, beelineActionList)
		self.wumpusLocProb = np.ndarray(shape=(4,4))
		self.pitLocProb = np.ndarray(shape=(4,4))
		self.riskProb = np.ndarray(shape=(4,4))
		# initialize wumpus location prob
		self.wumpusLocProb = WumpusLocationProb.WumpusLocationProb()
		# initialize pit location prob
		self.pitLocProb = PitLocationProb.PitLocationProb()
		# initialize risk location prob
		for i in range(4):
			for j in range(4):
				self.riskProb[i][j] = 1 - (1 - 1/15)*(1 - 0.2)
		self.riskProb[0][0] = 0		
		# initialize queue
		self.unexploredQueue = []
		for i in range(4):
			for j in range(4):
				if i != 0 or j != 0:
					heappush(self.unexploredQueue, (np.linalg.norm((i-0, j-0)), Environment.Coords(i+1, j+1)))		

	def updateRisk(self, loc: Environment.Coords, stench:bool, breeze:bool):
		self.wumpusLocProb.updateWumpusProb(loc, stench)
		self.pitLocProb.updatePitProb(loc, breeze)
		for i in range(4):
			for j in range(4):
				if i != 0  or j != 0:
					self.riskProb[i][j] = 1 - (1 - self.wumpusLocProb.wumpusProb[i][j])\
						* (1 - self.pitLocProb.pitProb[i][j])		

	def checkNextUnexplored(self):
		for i in range(len(self.unexploredQueue)):
			nextLoc = heappop(self.unexploredQueue)
			if self.riskProb[nextLoc[1].x - 1][nextLoc[1].y - 1] < 0.5:
				return nextLoc[1]
		return None


	def nextAction(self, agentState: Environment.AgentState, percept: Environment.Percept) -> Environment.Action:
		nextLoc = Environment.Coords(0,0)
		# Safe location if not terminated
		if not agentState.hasGold:
			self.updateRisk(agentState.location, percept.stench, percept.breeze)
			self.safeLocations.add(agentState.location)
			nextLoc = self.checkNextUnexplored()
		# Climb when hasGold and at (1,1)
		if agentState.hasGold and agentState.location == Environment.Coords(1,1):
			return Environment.Action.Climb
		# Grab when found gold
		if percept.glitter and not agentState.hasGold:
			self.goldLocation = agentState.location
			self.shortestPath = self._bfs_shortestpath()
			return Environment.Action.Grab
		# Go back to Origin when hasGold
		if agentState.hasGold:
			if agentState.orientation != self._requireOrientation():
				return self._turn(agentState.orientation, self._requireOrientation())
			else:
				self.shortestPath.pop(0)
				return Environment.Action.Forward
		# Other random
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
