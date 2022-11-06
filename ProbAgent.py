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
	lowRiskLocs:	set
	targetLoc:		Environment.Coords
	giveUp:			bool
	hasArrow:		bool
	wumpusAlive:	bool
	doShoot:		bool
	noWumMissShot:	list

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
		self.lowRiskLocs = set()
		for i in range(4):
			for j in range(4):
				if i != 0 or j != 0:
					self.unexploredLocs.add(Environment.Coords(i+1, j+1))	
		# initial target loc
		self.targetLoc = Environment.Coords(1, 1)
		self.giveUp = False
		self.hasArrow = True
		self.wumpusAlive = True
		self.doShoot = False
		self.noWumMissShot = []

	def _updateRisk(self, loc: Environment.Coords, stench:bool, breeze:bool):
		self.lowRiskLocs = set()

		if self.wumpusAlive:
			self.wumpusLocProb.updateWumpusProb(loc, stench, len(self.unexploredLocs), missShot=False)
			if len(self.noWumMissShot) != 0:
				for loca in self.noWumMissShot:
					self.wumpusLocProb.updateWumpusProb(loca, stench, len(self.unexploredLocs), missShot=True)
		else:
			for i in range(4):
				for j in range(4):
					self.wumpusLocProb.wumpusProb[i][j] = 0

		self.pitLocProb.updatePitProb(loc, breeze)
		for i in range(4):
			for j in range(4):
				if i != 0  or j != 0:
					self.riskProb[i][j] = 1 - (1 - self.wumpusLocProb.wumpusProb[i][j])\
						* (1 - self.pitLocProb.pitProb[i][j])	
					if self.riskProb[i][j] < 0.15:
						self.lowRiskLocs.add(Environment.Coords(i+1, j+1))

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
				if (coord != None) and (coord in self.safeLocations or coord == desti or coord in self.lowRiskLocs) and (not coord in visited):
				# if (coord != None) and  (not coord in visited):
					explored.append(coord)
					path_dict.update({coord:curr})
					visited.append(coord)
			if len(explored) > 0:
				curr = explored.pop(0)
			else:
				return []
			# if len(explored) != 0:
			# 	curr = explored.pop(0)
			# else:
			# 	return path
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
		numQ = len(unexploreQueue)
		for i in range(numQ):
			nearLoc = heappop(unexploreQueue)
			x = nearLoc[1].x
			y = nearLoc[1].y
			if self.riskProb[x-1][y-1] < 0.51:
				nextLoc = nearLoc[1]
				path = self._bfs_shortestpath(agentLoc, nextLoc)
				if len(path) == 0:
					continue
				else:
					break
		if path:
			return nextLoc, path
		else:
			self.giveUp = True
			return Environment.Coords(1,1), self._bfs_shortestpath(agentLoc, Environment.Coords(1,1))

	def _shoot(self, loc:Environment.Coords):
		for coord in self._adjacent(loc, 4, 4):
			if coord != None and self.wumpusLocProb.wumpusProb[coord.x-1][coord.y-1] > 0.4999:
				return True, coord
		return False, None

	def _requireOrientation(self, start, next):
		if start.x == next.x and start.y > next.y:
			return Environment.Orientation.South
		elif start.x == next.x and start.y < next.y:
			return Environment.Orientation.North
		elif start.x > next.x and start.y == next.y:
			return Environment.Orientation.West
		elif start.x < next.x and start.y == next.y:
			return Environment.Orientation.East
		else:
			print("short path error")

	def _notwumpusInLineOfFire(self, agentState: Environment.AgentState):
		if agentState.orientation == Environment.Orientation.West:
			return [Environment.Coords(x, agentState.location.y) for x in range(1, 5) if x < agentState.location.x]
		elif agentState.orientation == Environment.Orientation.East:
			return [Environment.Coords(x, agentState.location.y) for x in range(1, 5) if x > agentState.location.x]
		elif agentState.orientation == Environment.Orientation.North:
			return [Environment.Coords(agentState.location.x, y) for y in range(1, 5) if y > agentState.location.y]
		elif agentState.orientation == Environment.Orientation.South:
			return [Environment.Coords(agentState.location.x, y) for y in range(1, 5) if y < agentState.location.y]           


	def nextAction(self, agentState: Environment.AgentState, percept: Environment.Percept) -> Environment.Action:
		# update risk
		self._updateRisk(agentState.location, percept.stench, percept.breeze)
		# shoot
		if self.hasArrow and self.wumpusAlive:
			self.doShoot, aim = self._shoot(agentState.location)

		if self.doShoot and self.hasArrow:
			
			if agentState.orientation != self._requireOrientation(agentState.location, aim):
				return self._turn(agentState.orientation, self._requireOrientation(agentState.location, aim))
			else:
				self.hasArrow = False
				return Environment.Action.Shoot

		if self.doShoot and (not self.hasArrow):
			#just shoot with previous move
			self.doShoot = False
			if percept.scream:
				# wumpus dead
				self.wumpusAlive = False
				self._updateRisk(agentState.location, percept.stench, percept.breeze)
				
			else:
				# miss the shoot
				self.noWumMissShot = self._notwumpusInLineOfFire(agentState)
				self._updateRisk(agentState.location, percept.stench, percept.breeze)


		# Remove Unexplored
		if agentState.location in self.unexploredLocs:
			self.unexploredLocs.remove(agentState.location)

		# Climb when hasGold and at (1,1)
		if (self.giveUp or agentState.hasGold) and agentState.location == Environment.Coords(1,1):
			return Environment.Action.Climb
		# Grab when found gold
		if percept.glitter and not agentState.hasGold:
			self.goldLocation = agentState.location
			self.targetLoc = Environment.Coords(1,1)
			self.shortestPath = self._bfs_shortestpath(agentState.location, Environment.Coords(1,1))
			return Environment.Action.Grab
		# Go back to Origin when hasGold
		if agentState.hasGold:
			if agentState.orientation != self._requireOrientation(self.shortestPath[0], self.shortestPath[1]):
				return self._turn(agentState.orientation, self._requireOrientation(self.shortestPath[0], self.shortestPath[1]))
			else:
				self.shortestPath.pop(0)
				return Environment.Action.Forward

		if (not agentState.hasGold) and (not self.giveUp):
			self.safeLocations.add(agentState.location)
			# One more check before move to target
			if len(self.shortestPath) == 2:
				unexploreQueue = []
				for loc in self.unexploredLocs:
					heappush(unexploreQueue, (self.riskProb[loc.x-1][loc.y-1], loc))
				unexploreQueue_loc = []
				curr = heappop(unexploreQueue)
				heappush(unexploreQueue_loc, (np.linalg.norm((curr[1].x-agentState.location.x, curr[1].y-agentState.location.y)), curr[1]))
				for i in range(len(unexploreQueue)-1):
					next = heappop(unexploreQueue)
					if np.abs(curr[0] - next[0]) <0.001:
						heappush(unexploreQueue_loc, (np.linalg.norm((next[1].x-agentState.location.x, next[1].y-agentState.location.y)), next[1]))
					else:
						break
				targetLoc_temp, shortestPath_temp = self._findNextLoc(agentState.location, unexploreQueue_loc)
				if targetLoc_temp == self.targetLoc:
					pass
				else:
					self.targetLoc = targetLoc_temp
					self.shortestPath = shortestPath_temp.copy()
				if len(self.shortestPath) <= 1:
					self.giveUp = True

			# 1. Plan for next target location			
			while agentState.location == self.targetLoc:
				# 1.1 Update unexplored queue
				unexploreQueue = []
				for loc in self.unexploredLocs:
					heappush(unexploreQueue, (self.riskProb[loc.x-1][loc.y-1], loc))
				unexploreQueue_loc = []
				curr = heappop(unexploreQueue)
				heappush(unexploreQueue_loc, (np.linalg.norm((curr[1].x-agentState.location.x, curr[1].y-agentState.location.y)), curr[1]))
				for i in range(len(unexploreQueue)-1):
					next = heappop(unexploreQueue)
					if np.abs(curr[0] - next[0]) <0.001:
						heappush(unexploreQueue_loc, (np.linalg.norm((next[1].x-agentState.location.x, next[1].y-agentState.location.y)), next[1]))
					else:
						break

				# 1.2 Find target location
				self.targetLoc, self.shortestPath = self._findNextLoc(agentState.location, unexploreQueue_loc)
				# # 1.3 Remove visited
				# if not self.giveUp:
				# 	self.unexploredLocs.remove(self.targetLoc)
			# 2. Go to target location
				if len(self.shortestPath) <= 1:
					self.giveUp = True
					self.targetLoc = Environment.Coords(1,1)
					self.shortestPath = self._bfs_shortestpath(agentState.location, Environment.Coords(1,1))
					break
			if not self.giveUp:
				if agentState.orientation != self._requireOrientation(self.shortestPath[0], self.shortestPath[1]):
					return self._turn(agentState.orientation, self._requireOrientation(self.shortestPath[0], self.shortestPath[1]))
				else:
					self.shortestPath.pop(0)
					return Environment.Action.Forward

		# Go back to Origin when hasGold
		if self.giveUp:
			if agentState.orientation != self._requireOrientation(self.shortestPath[0], self.shortestPath[1]):
				return self._turn(agentState.orientation, self._requireOrientation(self.shortestPath[0], self.shortestPath[1]))
			else:
				self.shortestPath.pop(0)
				return Environment.Action.Forward

		return None

	def visualizeRiskProb(self) -> str:
		st:list = []
		for y in range(self.gridHeight, 0, -1):
			for x in range(1, self.gridWidth+1):
				st.extend(str(np.around(self.riskProb[x-1][y-1],2)))
				if x != 4:
					st.append("|")
			st.append("\n")   
		return "".join(st)

	def visualizeWumpusProb(self) -> str:
		st:list = []
		for y in range(self.gridHeight, 0, -1):
			for x in range(1, self.gridWidth+1):
				st.extend(str(np.around(self.wumpusLocProb.wumpusProb[x-1][y-1],2)))
				if x != 4:
					st.append("|")
			st.append("\n")   
		return "".join(st)

	def visualizePitProb(self) -> str:
		st:list = []
		for y in range(self.gridHeight, 0, -1):
			for x in range(1, self.gridWidth+1):
				st.extend(str(np.around(self.pitLocProb.pitProb[x-1][y-1],2)))
				if x != 4:
					st.append("|")
			st.append("\n")   
		return "".join(st)

	def visualizeUnexplored(self) -> str:
		st:list = []
		for y in range(self.gridHeight, 0, -1):
			for x in range(1, self.gridWidth+1):
				show = "X" if Environment.Coords(x, y) in self.unexploredLocs else "O"
				st.extend(show)
				if x != 4:
					st.append("|")
			st.append("\n")   
		return "".join(st)

if __name__ == '__main__':
	probAgent =  ProbAgent()
	print(1)
