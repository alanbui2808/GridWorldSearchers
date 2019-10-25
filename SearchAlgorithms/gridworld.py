class Gridworld:
    states = None
    initial_state = None
    goal_state = None

    def __init__(self, filename):
        with open(filename) as file:
            self.states = [list(line) for line in file.read().splitlines()]
            for y, line in enumerate(self.states):
                for x, value in enumerate(line):
                    if value.isnumeric():
                        line[x] = int(value)
                    if value == 's':
                        self.initial_state = (x, y)
                    if value == 'g':
                        self.goal_state = (x, y)

    def successors(self, state):
        # TODO
        if self == None: 
            print("self is a null object") 
            return

        #Check the dimension (x,y) of the grid:
        grid = self.states
        successors_list = list() # List of coordinates (x,y)

        # (1). Width (x) of the grid:
        width_grid = len(grid[0])-1

        # (2). Length (y) of the grid
        length_grid = len(grid)-1
        
        # Note: (x,y) is a tuple while successor_list is a list of coordinates (x,y) of tuple.
        #       The grid and (x,y) is stored as 2D like Java but accessing (x,y) is like matrix: 
        #       grid[y][x] 
        ''' 
        Algorithm: if (x,y) is in the grid and self[y][x] is numerical or not a wall '#'; then
                   add it the successor list.
        '''

        # Check Left: (x-1, y)
        left_x = state[0] - 1
        
        if(left_x >= 0): 
            if(grid[state[1]][left_x] != '#'):
                successors_list.append((left_x, state[1]))

        # Chech Right (x+1, y)
        right_x = state[0] + 1
        
        if(right_x <= width_grid ):
            if(grid[state[1]][right_x] != '#'):
                successors_list.append((right_x, state[1]))

        # Check Down (since y-plane in 2D array grows downward): (x, y+1)
        down_y = state[1] + 1

        if(state[1] + 1 <= length_grid):
            if(grid[down_y][state[0]] != '#'):
                successors_list.append((state[0], down_y))

        # Check Up: (x, y-1)
        up_y = state[1] - 1
        if(state[1] - 1 >= 0):
            if(grid[up_y][state[0]] != '#'):
                successors_list.append((state[0], up_y))

        return successors_list



    def cost(self, state):
        # TODO
        if self == None:
            print("self is null")
            return

        # since we only process any node that is reachable (not a wall '#') therefore, no edge
        # edge case where of '#'.
        grid = self.states
        x = state[0]
        y = state[1]

        if(grid[y][x] == 's' or grid[y][x] == 'g'):
            return 1

        else:
            return grid[y][x]
