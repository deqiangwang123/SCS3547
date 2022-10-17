import Environment
import NaiveAgent

def main():
    agent = NaiveAgent.NaiveAgent()
    env = Environment.Environment()
    (env, percept) = env.new_game(4, 4, 0.2, False)
    env.visualize()
    # env.percept.show()
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
