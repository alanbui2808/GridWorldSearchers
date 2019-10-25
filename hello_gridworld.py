from assignment1.gridworld import Gridworld


def run():
    gridworld = Gridworld('gw/1.txt')
    print("Hello Gridworld!")
    print(gridworld.states)
    print(gridworld.initial_state)
    print(gridworld.goal_state)

    print(gridworld.successors((2,2)))

    
    

if __name__ == '__main__':
    run()
