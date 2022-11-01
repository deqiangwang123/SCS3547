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

    def __init__(self):
        self.gridHeight = 4
        self.gridWidth = 4
        self.breeze_memory = np.ndarray(shape=(4,4))
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

    def _adjacentCells(self, coords: Environment.Coords = Environment.Coords(1,1)) ->list:
        return [
            Environment.Coords(coords.x - 1, coords.y) if coords.x > 1 else None, # to left
            Environment.Coords(coords.x + 1, coords.y) if coords.x < self.gridWidth else None, # to right
            Environment.Coords(coords.x, coords.y - 1) if coords.y > 1 else None, # to down
            Environment.Coords(coords.x, coords.y + 1) if coords.y < self.gridHeight else None # to up
        ]
 
    def updatePitProb(self, loc:Environment.Coords, breeze:bool):
        # update memory based on correct loc's stech info
        self._updateBreezeMemory(loc, breeze)
        # Use a list to store the stech info for BN, the first None is wumpus location
        # Add 15 None for 15 pit locations
        breeze_checkout = []
        for i in range(15):
            breeze_checkout.append(None)
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
        # nearby loc
        for nearby_loc in self._adjacentCells(loc):
            if nearby_loc is not None:
                index = 4 * (nearby_loc.x - 1) + nearby_loc.y - 1
                prob = pit_loc[0][index].probability('T')
                self.pitProb[nearby_loc.x-1][nearby_loc.y-1] = prob       

if __name__ == '__main__':
    pP = PitLocationProb()
    pP.updatePitProb(Environment.Coords(1,1), False)
    pP.updatePitProb(Environment.Coords(2,1), False)
    print(pP.pitProb[2][0])

