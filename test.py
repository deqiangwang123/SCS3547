import AgentState as AS
import Environment as Env

def main():
    agent = AS.AgentState(Env.Coords(1,1), Env.Orientation.East, False, True, True)
    print(f"{agent.hasArrow}")

if __name__ == '__main__':
    main()