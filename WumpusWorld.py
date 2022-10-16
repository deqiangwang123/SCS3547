import random
import sys
import Environment as Env
import NaiveAgent_ as NAgent

def main():
    agent = NAgent.NaiveAgent(location=Env.Coords(1,1), orientation=Env.Orientation.East, 
        hasGold=False, hasArrow=True, isAlive=True)
    env = Env.Environment()
    (env, percept) = env.new_game(4, 4, 0.2, False)
    env.visualize()
    env.percept.show()
    total_award = env.percept.reward

    while not env.percept.isTerminated:
        nextAction = agent.nextAction(env.percept)
        (env, percept) = env.applyAction(nextAction)
        env.visualize()
        env.percept.show()
        total_award = total_award + env.percept.reward
        print(f"Total reward: {total_award}")


if __name__ == '__main__':
    main()
