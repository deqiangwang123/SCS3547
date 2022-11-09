import Environment
import ProbAgent

MAX_RUN = 1
PLOT_INFO = True
def main():
    total_award_all = []
    game = 0 
    for i in range(MAX_RUN):
        game = game +1
        print(game)
        agent = ProbAgent.ProbAgent()
        env = Environment.Environment()
        env = env.new_game(4, 4, 0.2, True)
        if PLOT_INFO:
            print(f"Step 0: \n")
            env.percept.show()
            print(f"{env.visualize()}")
        nextAction = agent.nextAction(env.agent, env.percept)
        if PLOT_INFO:
            print(f"nextAction: {nextAction} AgentLoc: ({env.agent.location.x}, {env.agent.location.y}) TargetLoc: ({agent.targetLoc.x}, {agent.targetLoc.y})\n")
            print(f"RiskProb:\n{agent.visualizeRiskProb()}")
            print(f"WumpusProb:\n{agent.visualizeWumpusProb()}")
            print(f"PitProb:\n{agent.visualizePitProb()}")      
            print(f"Unexplored:\n{agent.visualizeUnexplored()}") 
            print(agent.shortestPath) 

        step = 0
        total_award = env.percept.reward

        while not env.percept.isTerminated:
            step = step + 1
            if PLOT_INFO:
                print(f"Step {step}")   
            env = env.applyAction(nextAction)
            if PLOT_INFO:
                env.percept.show()
                print(f"{env.visualize()}") 
            nextAction = agent.nextAction(env.agent, env.percept)    
            if PLOT_INFO:      
                print(f"nextAction: {nextAction} AgentLoc: ({env.agent.location.x}, {env.agent.location.y}) TargetLoc: ({agent.targetLoc.x}, {agent.targetLoc.y})\n")
                print(f"RiskProb:\n{agent.visualizeRiskProb()}")
                print(f"WumpusProb:\n{agent.visualizeWumpusProb()}")
                print(f"PitProb:\n{agent.visualizePitProb()}")        
                print(f"Unexplored:\n{agent.visualizeUnexplored()}")
                # print(agent.shortestPath) 
                # print(agent.safeLocations)
            total_award = total_award + env.percept.reward
            if PLOT_INFO:
                print(f"Total reward: {total_award}\n")
        total_award_all.append(total_award)
    print(f"Total reward: {total_award_all}\n")
    print(f"Total reward: {sum(total_award_all)}\n")


if __name__ == '__main__':
    main()
