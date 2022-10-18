import Environment
import NaiveAgent

def main():
    agent = NaiveAgent.NaiveAgent()
    env = Environment.Environment()
    env = env.new_game(4, 4, 0.2, False)
    print(f"Step 0: \n")
    print(f"{env.visualize()}")
    step = 0
    # env.percept.show()
    total_award = env.percept.reward

    while not env.percept.isTerminated:
        step = step + 1
        nextAction = agent.nextAction(env.percept)
        env = env.applyAction(nextAction)
        print(f"Step {step} Action: {nextAction}")
        print(f"{env.visualize()}")
        env.percept.show()
        total_award = total_award + env.percept.reward
        print(f"Total reward: {total_award}\n")


if __name__ == '__main__':
    main()
