from .agent import Agent
from queue import PriorityQueue
import math


class AStar(Agent):
    def search(self, gridworld):
        pass
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
        max_int = 2^31

        # Distance list:
        distance = [max_int] * state_count

        # Path list:
        path = [0] * state_count

        # Found_Goal: True if goal is found after the Search
        found_goal = False

        # Initialising before A*:
        distance[state_hash[start]] = 0
        pq = PriorityQueue()
        pq.put((distance[state_hash[start]] + self.heuristic(start, goal), start))

        while not pq.empty():
        	current = pq.get() # current = (cost, (x,y))
        	

        	current_id = current[1]

        	if current_id == goal:
        		found_goal = True
        		break

        	expanded_nodes += 1
        	neighbor_list = gridworld.successors(current_id)

        	for i in range(len(neighbor_list)):
        		neighbor = neighbor_list[i]

        		new_distance = distance[state_hash[current_id]] + gridworld.cost(neighbor)

        		if new_distance < distance[state_hash[neighbor]]:

        			# Update the new distance[neighbor]
        			distance[state_hash[neighbor]] = new_distance

        			# Add the neighbor with the new distance + heuristic to the goal:
        			pq.put((distance[state_hash[neighbor]] + self.heuristic(neighbor, goal), neighbor))

        			# Set the path between current and neighbor
        			path[state_hash[neighbor]] = state_hash[current_id]


        # If after the Search, we have not found the goal_state
        if found_goal == False:
            print("There is no Path to the Goal")
            hreturn

        # Otherwise print the path, cost and expanded nodes:
        else:
            # Path before hash:
            path_hash = self.print_path(path, state_hash[start], state_hash[goal])

            # Result_path after hasing:
            result_path = list()

            for i in range(len(path_hash)):
                # We hash the value (index) back to the original state:
                state = index_hash[path_hash[i]]

                result_path.append(state)

        return result_path, distance[state_hash[goal]], expanded_nodes



############################################################################################



    def heuristic(self, node, goal):
    	goal_x = goal[0]
    	goal_y = goal[1]
    	node_x = node[0]
    	node_y = node[1]
		
		#return abs(goal_x - node_x) + abs(goal_y - node_y)

    	return int(math.sqrt((goal_y - node_y)**2 + (goal_x - node_x)**2))




############################################################################################
    def print_path(self, path, start, goal):
        if (start == goal): return goal

        result_path = list()

        while(True):
            result_path.insert(0, goal)
            goal = path[goal]

            if(goal == start):
                result_path.insert(0, start)
                break

        return result_path



