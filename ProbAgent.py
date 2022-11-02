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
	unexploredLocs: set
	targetLoc:		Environment.Coords

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
		# initialize unexplored set
		self.unexploredLocs = set()
		for i in range(4):
			for j in range(4):
				if i != 0 or j != 0:
					self.unexploredLocs.add(Environment.Coords(i+1, j+1))	
		# initial target loc
		self.targetLoc = Environment.Coords(1, 1)

	def _updateRisk(self, loc: Environment.Coords, stench:bool, breeze:bool):
		self.wumpusLocProb.updateWumpusProb(loc, stench)
		self.pitLocProb.updatePitProb(loc, breeze)
		for i in range(4):
			for j in range(4):
				if i != 0  or j != 0:
					self.riskProb[i][j] = 1 - (1 - self.wumpusLocProb.wumpusProb[i][j])\
						* (1 - self.pitLocProb.pitProb[i][j])		

	def _bfs_shortestpath(self, agentLoc:Environment.Coords, destination:Environment.Coords) -> list:
		path = []
		explored = []
		visited = []
		path_dict = {}
		desti = destination
		start = agentLoc
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
            # if curr == desti:
            #     path_dict.update({desti:curr})
        
		path.append(desti)
		prev_path = path_dict.get(desti)
		path.insert(0,prev_path)
		while prev_path != start:
			prev_path = path_dict.get(prev_path)
			path.insert(0,prev_path)
		return path

	def _findNextLoc(self, agentLoc: Environment.Coords, unexploreQueue:list):
		nextLoc = Environment.Coords(1, 1)
		path = []
		for i in range(len(unexploreQueue)):
			x = unexploreQueue[i][1].x
			y = unexploreQueue[i][1].y
			if self.riskProb[x-1][y-1] < 0.5:
				nextLoc = unexploreQueue[i][1]
				path = self._bfs_shortestpath(agentLoc, nextLoc)
				if path:
					return nextLoc, path
		return nextLoc, path
			

	def nextAction(self, agentState: Environment.AgentState, percept: Environment.Percept) -> Environment.Action:
		# update risk
		self._updateRisk(agentState.location, percept.stench, percept.breeze)

		if not agentState.hasGold:
			# 1. Plan for next target location
			if agentState.location == self.targetLoc:
				# 1.1 Update unexplored queue
				unexploreQueue = []
				for loc in self.unexploredLocs:
					heappush(unexploreQueue, (np.linalg.norm((loc.x-1, loc.y-1)), loc))
				# 1.2 Find target location
				self.targetLoc, self.shortestPath = self._findNextLoc(agentState.location, unexploreQueue)
			# 2. Go to target location
			else:
				if agentState.orientation != self._requireOrientation():
					return self._turn(agentState.orientation, self._requireOrientation())
				else:
					self.shortestPath.pop(0)
					return Environment.Action.Forward

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
		return None
		# Other random
		# randAction = random.randint(1, 4)
		# if randAction == 1:
		# 	return Environment.Action.Forward
		# if randAction == 2:
		# 	return Environment.Action.TurnLeft
		# if randAction == 3:
		# 	return Environment.Action.TurnRight
		# if randAction == 4:
		# 	return Environment.Action.Shoot                


if __name__ == '__main__':
	probAgent =  ProbAgent()
	print(1)
