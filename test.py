from Agent_State import AgentState as AS
import Environ as Env

def main():
    agent = AS(Env.Coords(1,1), Env.Orientation.East, False, True, True)
    print(f"{agent.hasArrow}")

if __name__ == '__main__':
    main()

    