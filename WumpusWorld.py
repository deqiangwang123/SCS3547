import random
import sys
import Environment as Env

def main():
    per_return = Env.Percept()
    per_return.show()
    a = " ".join(str(i) for i in range(10, 0, -1))
    print (a)

    # for y in range(4,0,-1):
    #     for x in range(4,0,-1):


if __name__ == '__main__':
    main()