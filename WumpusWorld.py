import random
import sys
import Environment as Env
import NaiveAgent as NAgent

def main():
    env = Env.Environment(gridWidth=4, gridHeight=4, pitProb=0.2,\
        allowClimbWithoutGold=False)
    agent = NAgent.Agent(location=Env.Coords(1,1), orientation=Env.Orientation.East, hasGold=False, hasArrow=True, isAlive=True)
    totalReward = 0
    MAX_EPISODE = 10
    terminated = False

    def runEpisode(env: Env.Environment, agent: NAgent) -> bool:
        nextAction = agent.NaiveAgent.nextAction(env.percept)
        print(f"Action: {nextAction}")
        env.applyAction(nextAction)
        print(env.visualize())
        env.percept.show()
        totalReward = totalReward + env.percept.reward
        return env.terminated
        
    for i in range(1, MAX_EPISODE):
        if not terminated:
            terminated = runEpisode(env, agent)
        else:
            break


if __name__ == '__main__':
    main()