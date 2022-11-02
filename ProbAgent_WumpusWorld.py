import Environment
import ProbAgent

def main():
    agent = ProbAgent.ProbAgent()
    env = Environment.Environment()
    env = env.new_game(4, 4, 0.2, False)
    print(f"Step 0: \n")
    print(f"{env.visualize()}")
    env.percept.show()
    step = 0
    total_award = env.percept.reward

    while not env.percept.isTerminated:
        step = step + 1
        nextAction = agent.nextAction(env.agent, env.percept)
        env = env.applyAction(nextAction)
        print(f"Step {step} Action: {nextAction} AgentLoc: ({env.agent.location.x}, {env.agent.location.y}) TargetLoc: ({agent.targetLoc.x}, {agent.targetLoc.y})\n")
        print(f"{env.visualize()}")
        print(f"{agent.visualize()}")
        env.percept.show()
        total_award = total_award + env.percept.reward
        print(f"Total reward: {total_award}\n")


if __name__ == '__main__':
    main()
