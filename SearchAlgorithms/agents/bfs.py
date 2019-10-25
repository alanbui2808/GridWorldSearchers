from .agent import Agent
from collections import deque


class BFS(Agent):
    def search(self, gridworld):
        # TODO

        start = gridworld.initial_state
        goal = gridworld.goal_state

        # state_hash to convert (x,y) to simple index from 0 -> n^2 
        # and an index_hash to map back: 
        state_hash = {} # {(x,y) -> int}
        index_hash = {} # {int -> (x,y)}
        state_count = 0

        for x in range(len(gridworld.states[0])):
            for y in range(len(gridworld.states)):
                state_hash[(x,y)] = state_count
                index_hash[state_count] = (x,y)
                state_count += 1

        # Setting up:
        expanded_nodes = 0 

        # Visited[size = state_count + 1]:
        visited = [False] * state_count

        # Distance array:
        distance = [0] * state_count

        # Path array
        path = [0] * state_count

        # Found Goal: Check if the goal is discovered after the search:
        found_goal = False

        # Initializing before BFS
        queue = deque()
        queue.append(start)
        visited[state_hash[start]] = True
        distance[state_hash[start]] = 0

        # BFS:
        while queue:
            current = queue.popleft()
            
            
            if (current == goal):
                found_goal = True
                break

            expanded_nodes += 1
            neighbors_list = gridworld.successors(current)
            
            for i in range(len(neighbors_list)):
                neighbor = neighbors_list[i]
                '''
                if(neighbor == goal): 
                    found_goal = True

                    distance[state_hash[neighbor]] += distance[state_hash[current]] + gridworld.cost(neighbor)
                    path[state_hash[neighbor]] = state_hash[current]
                    break
                '''

                if(visited[state_hash[neighbor]] == False):
                    visited[state_hash[neighbor]] = True
                    queue.append(neighbor)

                    distance[state_hash[neighbor]] += distance[state_hash[current]] + gridworld.cost(neighbor)
                    path[state_hash[neighbor]] = state_hash[current]

        # If after the algorithm , we visited all the reachable nodes and still could not discovered
        # the goal node:
        if found_goal == False: 
            print("There is no Path to the Goal")
            return

        # Otherwise print cost, path and goal node:
        else:   
            # path before hash:
            path_hash = self.print_path(path, state_hash[start], state_hash[goal])

            # result_path after hashing:
            result_path = list()

            for i in range(len(path_hash)):
                # We hash the value (index) back to the orginal state:
                state = index_hash[path_hash[i]]

                result_path.append(state)
        
        return result_path, distance[state_hash[goal]], expanded_nodes 


    # Print path function: 
    def print_path(self, path, start, goal):
        if(start == goal): return goal

        result_path = list()

        while(True):
            result_path.insert(0, goal)
            goal = path[goal]

            if(goal == start):
                result_path.insert(0, start)
                break;

        return result_path
        
