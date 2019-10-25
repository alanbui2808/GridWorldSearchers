
# Search Algorithms

## Preliminary: Gridworlds

*Gridworlds* are a type of environment that are frequently used in AI research.
They are designed to model at an abstract level the problem of navigating in a physical environment.
Generally, the task is to find the path from *initial state* to some other *goal state* with the lowest cost.
There may be obstacles or hazards in the world that the agent needs to avoid on its way to the goal.
In this project, there are implementations of 4 iconic searches for shortest-path problems:
breadth-first search (BFS), uniform cost search (UCS), greedy best-first search (GBFS), and A*.  

In this project, gridworlds are specified in text files.
Each gridworld is a discrete, two-dimensional environment.
Each state is referenced by a tuple, `(x, y)`, where `x` represents the column and `y` represents the row.
The top-left state is always `(0, 0)`.
In each state, the agent can move up, down, left, or right (but not diagonally).
However, the agent may not go "off the grid" (even if it wishes to avoid paying taxes).
Consider the gridworld specified in the file `gw/1.txt`:

```
s11
#21
g11
```

Each character in the file corresponds to a single state.
The character `s` specifies the initial state (in this case, `(0, 0)`).
The character `g` specifies the goal state (in this case, `(0, 2)`).
The character `#` specifies a wall. For instance, in this example, the agent cannot enter `(0, 1)`.
Another way of thinking about this is that the state *doesn't exist*; that is, there is no state corresponding to `(0, 1)`.
For every other state, the character specifies the cost of entering that state, which can be any integer from 0 to 9.
For example, the cost of entering `(1, 0)` is 1, whereas the cost of entering `(2, 0)` is 2.
The cost of entering the initial or goal state is always 1.
However, because the agent *starts* in the initial state, its cost should not be counted when considering the total path, unless it was reentered.
On the other hand, the cost of entering the goal state should *always* be counted.

## Four Search Algorithms

1. Breadth-first search (`BFS`)
2. Uniform cost search (`UCS`)
3. Greedy best-first search (`GBFS`)
4. A* (`AStar`)

Each of them should be in the appropriate file in `assignment1/agents`.
The `search` for each class function should return three things:

1. An array of tuples representing the solution path,
2. The cost of the solution,
3. The number of nodes expanded during the search.

We provided a run script which may be used to test the agents.
For an example, we also included a `RandomSearch` agent which searches randomly for a solution, and returns the first path found.
The run script may be used as follows:

```
python run.py random gw/0.txt
```

This will run the random agent on example Gridworld 0 stored in `gw/0.txt`.
If you implemented the gridworld correctly, you should see output that looks like:

```
solution [(0, 0), (1, 0), (0, 0), (1, 0), (1, 1)]
cost 4
nodes_expanded 4
```

In general, to invoke the `run.py` script, you should run
```
python run.py [agent] [gw]
```
where `[agent]` is one of the strings `bfs`, `ucs`, `gbfs`, `astar`, or `random`, and `[gw]` is the file path to a gridworld text file (all parts of this command are case sensitive).

### Heuristics
For this project, we use Euclidean Distance to calculate the heuristic from a given node to the goal. You may also use other heuristic to compare such as Manhattan Distance, etc.

## Analysis of different Searches
We would like to conduct these experiments below to see how different searches may behave differently under variety of environments. Below are 4 tested environemnts:

1. A girdworld example where BFS returns the optimal solution
2. A gridworld example where GBFS returns a suboptimal solution
3. A gridworld example where GBFS returns the optimal solution while expanding fewer nodes than A*
4. A gridworld example where A* expands fewer nodes than UCS

Each experiment is stored in a text file in the `example` folder.
For example, the experiment 1 should be put in `example/1.txt`.
