import random
import sys
import Environ as Env
import NaiveAgent_ as NAgent

def main():
    env = Env.Environment(gridWidth=4, gridHeight=4, pitProb=0.2,\
        allowClimbWithoutGold=False)
    agent = NAgent.NaiveAgent(location=Env.Coords(1,1), orientation=Env.Orientation.East, hasGold=False, hasArrow=True, isAlive=True)
    totalReward = 0
    MAX_EPISODE = 10
    terminated = False

    def runEpisode(env: Env.Environment, agent: NAgent.NaiveAgent) -> bool:
        nextAction = agent.nextAction(env.percept)
        print(f"Action: {nextAction}")
        env.applyAction(nextAction)
        print(env.visualize())
        env.percept.show()       
        return env.terminated, env.percept.reward
        
    for i in range(1, MAX_EPISODE):
        if not terminated:
            terminated, reward = runEpisode(env, agent)
            totalReward = totalReward + reward
        else:
            break


if __name__ == '__main__':
    main()