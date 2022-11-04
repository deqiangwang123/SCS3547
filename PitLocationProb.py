import Environment
import pomegranate
import numpy as np
import PitBreezeGraph
np.random.seed(42)

class PitLocationProb():
    breeze_memory: np.ndarray
    pitProb: np.ndarray
    gridWidth: int
    gridHeight: int
    notPitLoc: list

    def __init__(self):
        self.gridHeight = 4
        self.gridWidth = 4
        self.breeze_memory = np.ndarray(shape=(4,4))

        self.notPitLoc = []
        for i in range(15):
            self.notPitLoc.append(None)

        for i in range(4):
            for j in range(4):
                self.breeze_memory[i][j] = np.nan
        self.pitProb = np.ndarray(shape=(4,4))
        for i in range(4):
            for j in range(4):
                self.pitProb[i][j] = 0.2
        self.pitProb[0][0] = 0

    def _updateBreezeMemory(self, loc:Environment.Coords, breeze:bool):
        self.breeze_memory[loc.x-1][loc.y-1] = 1 if breeze else 0

    def _updateNotPitLoc(self, loc:Environment.Coords):
        if loc.x != 1 or loc.y != 1:
            self.notPitLoc[(loc.x - 1) * 4 + loc.y - 2] = 'F'
        return self.notPitLoc

    def updatePitProb(self, loc:Environment.Coords, breeze:bool):
        # update memory based on correct loc's stech info
        self._updateBreezeMemory(loc, breeze)
        # Use a list to store the stech info for BN, the first None is wumpus location
        # Add 15 None for 15 pit locations
        breeze_checkout = self._updateNotPitLoc(loc).copy()
        # Traverse Breeze locations
        for i in range(4):
            for j in range(4):
                if self.breeze_memory[i][j] == 1:
                    breeze_checkout.append('T')
                elif self.breeze_memory[i][j] == 0:
                    breeze_checkout.append('F')
                else:
                    breeze_checkout.append(None)
        # Predict the wumpus location
        pit_loc = PitBreezeGraph.pit_model.predict_proba([breeze_checkout])
        # Update all location
        for i in range(4):
            for j in range(4):
                if i != 0 or j != 0:
                    index = 4 * i + j -1
                    if pit_loc[0][index] == 'F':
                        self.pitProb[i][j] = 0
                    else:
                        prob = pit_loc[0][index].probability('T')
                        self.pitProb[i][j] = prob
    
if __name__ == '__main__':
    pP = PitLocationProb()
    pP.updatePitProb(Environment.Coords(1,1), False)
    pP.updatePitProb(Environment.Coords(2,1), True)
    print(pP.pitProb[0][0])
    print(pP.pitProb[1][1])
    print(pP.pitProb[1][0])
    print(pP.pitProb[2][0])

