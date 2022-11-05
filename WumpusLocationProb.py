import Environment
import pomegranate
import numpy as np
import WumStenchGraph
np.random.seed(42)

class WumpusLocationProb():
    stench_memory: np.ndarray
    wumpusProb: np.ndarray
    gridWidth: int
    gridHeight: int
    wumpusGraph: WumStenchGraph.WumStechGraph
    wumDict: dict

    def __init__(self):
        self.gridHeight = 4
        self.gridWidth = 4
        self.stench_memory = np.ndarray(shape=(4,4))
        for i in range(4):
            for j in range(4):
                self.stench_memory[i][j] = np.nan
        self.wumpusProb = np.ndarray(shape=(4,4))
        for i in range(4):
            for j in range(4):
                self.wumpusProb[i][j] = 1/15
        self.wumpusProb[0][0] = 0
        self.wumpusGraph = WumStenchGraph.WumStechGraph()
        self.wumpusGraph.bakeModel()
        self.wumDict = {}
        self.wumDict["1_2"] = 1./15
        self.wumDict["1_3"] = 1./15
        self.wumDict["1_4"] = 1./15
        self.wumDict["2_1"] = 1./15
        self.wumDict["2_2"] = 1./15
        self.wumDict["2_3"] = 1./15
        self.wumDict["2_4"] = 1./15
        self.wumDict["3_1"] = 1./15
        self.wumDict["3_2"] = 1./15
        self.wumDict["3_3"] = 1./15
        self.wumDict["3_4"] = 1./15
        self.wumDict["4_1"] = 1./15
        self.wumDict["4_2"] = 1./15
        self.wumDict["4_3"] = 1./15
        self.wumDict["4_4"] = 1./15

    def _updateStenchMemory(self, loc:Environment.Coords, stench:bool):
        self.stench_memory[loc.x-1][loc.y-1] = 1 if stench else 0

    def _updateNotWumpus(self, loc:Environment.Coords, safeNum:int):
        if loc.x != 1 or loc.y != 1:
            name = ''.join([str(loc.x), '_', str(loc.y)])
            if self.wumDict[name] != 0:
                self.wumDict[name] = 0
        for i in range(4):
            for j in range(4):
                if i != 0  or j != 0:
                    name = ''.join([str(i+1), '_', str(j+1)])
                    if self.wumDict[name] != 0:
                        self.wumDict[name] = 1./safeNum
        self.wumpusGraph.setWumpus_loc_prob(self.wumDict)
        self.wumpusGraph.bakeModel()

    def updateWumpusProb(self, loc:Environment.Coords, stench:bool, safeNum:int, missShot: bool):
        # update memory based on correct loc's stech info
        self._updateNotWumpus(loc, safeNum)
        if not missShot:
            self._updateStenchMemory(loc, stench)
        # Use a list to store the stech info for BN, the first None is wumpus location
        stench_checkout = [None]
        for i in range(4):
            for j in range(4):
                if self.stench_memory[i][j] == 1:
                    stench_checkout.append('T')
                elif self.stench_memory[i][j] == 0:
                    stench_checkout.append('F')
                else:
                    stench_checkout.append(None)
        # Predict the wumpus location
        wum_loc = self.wumpusGraph.wumpus_model.predict_proba([stench_checkout])
        # nearby loc
        for i in range(4):
            for j in range(4):
                if i != 0  or j != 0:
                    name = ''.join([str(i+1), '_', str(j+1)])
                    prob = wum_loc[0][0].probability(name)
                    self.wumpusProb[i][j] = prob

if __name__ == '__main__':
    wP = WumpusLocationProb()
    wP.updateWumpusProb(Environment.Coords(1,1), False, 14, False)
    wP.updateWumpusProb(Environment.Coords(2,1), True, 13, False)
    wP.updateWumpusProb(Environment.Coords(3,1), False, 12, False)
    # dict_1 = {}
    # dict_1['2_1'] = 0.4999
    print(wP.wumpusProb[1][0])
    print(wP.wumpusProb[2][0])

