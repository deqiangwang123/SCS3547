import Agent
import Environment as Env
import random

class NaiveAgent(Agent.Agent):
    def nextAction(self, percept: Env.Percept) -> Env.Action:
        randAction = random.randint(1, 6)
        if randAction == 1:
            return Env.Action.Forward
        if randAction == 2:
            return Env.Action.TurnLeft
        if randAction == 3:
            return Env.Action.TurnRight
        if randAction == 4:
            return Env.Action.Shoot
        if randAction == 5:
            return Env.Action.Grab
        if randAction == 6:
            return Env.Action.Climb                        
            