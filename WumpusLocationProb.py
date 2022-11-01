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

    def _updateStenchMemory(self, loc:Environment.Coords, stench:bool):
        self.stench_memory[loc.x-1][loc.y-1] = 1 if stench else 0

    def _adjacentCells(self, coords: Environment.Coords = Environment.Coords(1,1)) ->list:
        return [
            Environment.Coords(coords.x - 1, coords.y) if coords.x > 1 else None, # to left
            Environment.Coords(coords.x + 1, coords.y) if coords.x < self.gridWidth else None, # to right
            Environment.Coords(coords.x, coords.y - 1) if coords.y > 1 else None, # to down
            Environment.Coords(coords.x, coords.y + 1) if coords.y < self.gridHeight else None # to up
        ]

    def updateWumpusProb(self, loc:Environment.Coords, stench:bool):
        # update memory based on correct loc's stech info
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
        wum_loc = WumStenchGraph.wumpus_model.predict_proba([stench_checkout])
        # nearby loc
        for nearby_loc in self._adjacentCells(loc):
            if nearby_loc is not None:
                name = ''.join([str(nearby_loc.x), '_', str(nearby_loc.y)])
                prob = wum_loc[0][0].probability(name)
                self.wumpusProb[nearby_loc.x-1][nearby_loc.y-1] = prob

if __name__ == '__main__':
    wP = WumpusLocationProb()
    wP.updateWumpusProb(Environment.Coords(1,1), False)
    wP.updateWumpusProb(Environment.Coords(2,1), True)
    # dict_1 = {}
    # dict_1['2_1'] = 0.4999
    print(wP.wumpusProb[2][0])

