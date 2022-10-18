import Environment
import BeelineAgent

def main():
    agent = BeelineAgent.BeelineAgent()
    env = Environment.Environment()
    env = env.new_game(4, 4, 0.2, False)
    print(f"Step 0: \n")
    print(f"{env.visualize()}")
    env.percept.show()
    step = 0
    total_award = env.percept.reward

    # print(f"{agent._adjacent(Environment.Coords(1,2), 4, 4)}")
    while not env.percept.isTerminated:
        step = step + 1
        nextAction = agent.nextAction(env.agent, env.percept)
        env = env.applyAction(nextAction)
        print(f"Step {step} Action: {nextAction}\n")
        print(f"{env.visualize()}")
        env.percept.show()
        total_award = total_award + env.percept.reward
        print(f"Total reward: {total_award}\n")


if __name__ == '__main__':
    main()
