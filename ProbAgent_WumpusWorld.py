import Environment
import ProbAgent

def main():
    agent = ProbAgent.ProbAgent()
    env = Environment.Environment()
    env = env.new_game(4, 4, 0.2, False)
    print(f"Step 0: \n")
    env.percept.show()
    print(f"{env.visualize()}")
    nextAction = agent.nextAction(env.agent, env.percept)
    print(f"nextAction: {nextAction} AgentLoc: ({env.agent.location.x}, {env.agent.location.y}) TargetLoc: ({agent.targetLoc.x}, {agent.targetLoc.y})\n")
    print(f"RiskProb:\n{agent.visualizeRiskProb()}")
    print(f"WumpusProb:\n{agent.visualizeWumpusProb()}")
    print(f"PitProb:\n{agent.visualizePitProb()}")      
    print(f"Unexplored:\n{agent.visualizeUnexplored()}") 

    step = 0
    total_award = env.percept.reward

    while not env.percept.isTerminated:
        step = step + 1
        print(f"Step {step}")
        env = env.applyAction(nextAction)
        env.percept.show()
        print(f"{env.visualize()}") 
        nextAction = agent.nextAction(env.agent, env.percept)          
        print(f"nextAction: {nextAction} AgentLoc: ({env.agent.location.x}, {env.agent.location.y}) TargetLoc: ({agent.targetLoc.x}, {agent.targetLoc.y})\n")
        print(f"RiskProb:\n{agent.visualizeRiskProb()}")
        print(f"WumpusProb:\n{agent.visualizeWumpusProb()}")
        print(f"PitProb:\n{agent.visualizePitProb()}")        
        print(f"Unexplored:\n{agent.visualizeUnexplored()}")
        total_award = total_award + env.percept.reward
        print(f"Total reward: {total_award}\n")


if __name__ == '__main__':
    main()
