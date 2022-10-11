import Agent
import Environment as Env
import random

class NaiveAgent(Agent):
    def __init__(self, location:Env.Coords, orientation:Env.Orientation, hasGold: bool, hasArrow: bool, isAlive: bool):
        super().__init__(self, location:Env.Coords, orientation:Env.Orientation, hasGold: bool, hasArrow: bool, isAlive: bool)

    def nextAction(percept: Env.Percept) -> Env.Action:
        randAction = random.randint(1, 6)
        match randAction:
            case 1:
                return Env.Action.Forward
            case 2:
                return Env.Action.TurnLeft
            case 3:
                return Env.Action.TurnRight
            case 4:
                return Env.Action.Shoot
            case 5:
                return Env.Action.Grab
            case 6:
                return Env.Action.Climb