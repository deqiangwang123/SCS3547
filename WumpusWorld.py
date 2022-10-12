import random
import sys
import Environment as Env
import NaiveAgent_ as NAgent

# def main():
#     env = Env.Environment(gridWidth=4, gridHeight=4, pitProb=0.2,\
#         allowClimbWithoutGold=False)
#     agent = NAgent.NaiveAgent(location=Env.Coords(1,1), orientation=Env.Orientation.East, hasGold=False, hasArrow=True, isAlive=True)
#     totalReward = 0
#     MAX_EPISODE = 2
#     terminated = False

def runEpisode(env1: Env.Environment, agent: NAgent.NaiveAgent) -> bool:
    nextAction = agent.nextAction(env1.percept)
    print(f"Action: {nextAction}")
    env1.applyAction(nextAction)
    print(env1.visualize())
    env1.percept.show()       
    return env1.terminated, env1.percept.reward
        
#     for i in range(1, MAX_EPISODE):
#         if not terminated:
#             terminated, reward = runEpisode(env, agent)
#             totalReward = totalReward + reward
#         else:
#             break


if __name__ == '__main__':
    env = Env.Environment(gridWidth=4, gridHeight=4, pitProb=0.2,\
        allowClimbWithoutGold=False)
    print(f"{env.gridHeight}, {env.goldLocation.x}, {env.goldLocation.y}, {env.wumpusLocation.x}, {env.wumpusLocation.y}")
    agent = NAgent.NaiveAgent(location=Env.Coords(1,1), orientation=Env.Orientation.East, hasGold=False, hasArrow=True, isAlive=True)
    totalReward = 0
    MAX_EPISODE = 100
    terminated = False

    for i in range(1, MAX_EPISODE):
        if not terminated:
            terminated, reward = runEpisode(env, agent)
            totalReward = totalReward + reward
            print(f"Total reward: {totalReward}")
        else:
            break
