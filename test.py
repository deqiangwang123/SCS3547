import Environment
import NaiveAgent

def main():
    agent = NaiveAgent.NaiveAgent()
    env = Environment.Environment()
    print(f"{env.agent.location.x}")


if __name__ == '__main__':
    main()