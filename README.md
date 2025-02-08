# Pathfinding algorithms

## Table of Contents
- [Description](#Description)
- [BFS (Breadth-First Search) Algorithm](#1-bfs-breadth-first-search)
- [Greedy Algorithm](#2-greedy-algorithm)
- [A* Algorithm](#3-a-algorithm)
- [Experiment Algorithms with Larger Maps](#experiment-algorithms-with-larger-maps)
  - [300x300 Map](#300-x-300-map)
  - [600x600 Map](#600-x-600-map)
  - [900x900 Map](#900-x-900-map)
- [Conclusion](#conclusion)

## Description
This project examines and explains three fundamental pathfinding algorithms, each with distinct strategies and use cases:

1. BFS (Breadth-First Search) algorithm
2. Greedy algorithm
3. A* algorithm

## 1. BFS (Breadth-First Search)

### What is the BFS Algorithm and How Does It Work?
Breadth-First Search (BFS) is a graph traversal algorithm that starts at the root node and explores all nodes at the current depth before moving on to the next depth level.
It visits all the nodes at each depth level sequentially before proceeding to the nodes at the following depth.

#### Here’s the step-by-step process of the BFS algorithm:
1. Start at the root node and mark it as visited.
2. Add the root node to a queue.
3. While the queue is not empty:
   * Remove the first node from the queue and examine it.
   * For each unvisited neighbor of the node:
     * Mark the neighbor as visited. 
     * Add the neighbor to the end of the queue.
4. Repeat step 3 until the queue is empty.

BFS is commonly used to find the shortest path between two nodes in an unweighted graph, and it can also be used to detect cycles in a graph.
The time complexity of BFS is O(V+E), where V is the number of vertices (nodes) and E is the number of edges in the graph.

### Test map
Iterations: 188
```
*********************************
*     **********************    *
*   *******   D....**********   *
*   *******       .             *
* ****************.   ***********
************.......   ********  *
*           .********************
* ********  . *******************
*********   .               *****
******      .************       *
****        .......*********    *
**      ******    . *************
******************.      ********
****      ****   ..       ***** *
*                .              *
*                s              *
*********************************
```

## 2. Greedy Algorithm

### What is the Greedy Algorithm and How Does It Work?
A greedy algorithm is an approach that makes the locally optimal choice at each step with the goal of finding a global optimum solution.
It is a simple and efficient method commonly used to solve optimization problems.

#### The greedy algorithm typically works as follows:
1. Define a set of candidate solutions.
2. At each step, choose the best solution from the candidates based on specific criteria, usually selecting the one that provides the maximum benefit or the minimum cost. 
3. Remove any elements that conflict with the chosen solution.
4. Repeat steps 2 and 3 until a complete solution is found. 

Greedy algorithms are commonly used in optimization problems such as the knapsack problem, scheduling, and finding the minimum spanning tree.
However, it is important to note that greedy algorithms do not always yield an optimal solution for every problem.
In some cases, making a locally optimal choice at each step can lead to a suboptimal global solution.
Therefore, it is crucial to carefully evaluate the correctness and efficiency of the algorithm before applying it to a specific problem.

### Test map
Iterations: 34
```
*********************************
*     **********************    *
*   *******   D.   **********   *
*   *******    ....             *
* ****************.   ***********
************.......   ********  *
*           .********************
* ********  . *******************
*********   .               *****
******      .************       *
****        .......*********    *
**      ******    . *************
******************.      ********
****      ****   ..       ***** *
*                .              *
*                s              *
*********************************
```

## 3. A* Algorithm

### What is the A* Algorithm and How Does It Work?
A* (pronounced "A-star") is a heuristic search algorithm commonly used for pathfinding and graph traversal problems.
It is an extension of Dijkstra's algorithm and utilizes a heuristic function to estimate the distance to the goal node.

The A* algorithm works by maintaining two lists of nodes: an open list and a closed list.
The open list contains nodes that have been visited but not yet fully explored,
while the closed list contains nodes that have been fully explored.


#### Here's the step-by-step process of the A* algorithm:
1. Initialize the open list with the start node and the closed list as empty.
2. Calculate the heuristic cost from the current node to the goal node.
3. While the open list is not empty:
   * Choose the node with the lowest cost in the open list.
   * If the chosen node is the goal node, return the path.
   * Otherwise, move the chosen node from the open list to the closed list.
   * For each neighboring node of the chosen node:
     * Calculate the total cost to reach the neighboring node.
     * If the neighboring node is not in the open or closed list, add it to the open list.
     * If the neighboring node is in the open or closed list, update its cost if the new cost is lower.
4. If the goal node is not found, there is no path.

The time complexity of the A* algorithm depends on several factors, including the size of the search space,
the heuristic function used, and the efficiency of the data structures used to implement the algorithm.
In practice, the A* algorithm often performs much better than its worst-case time complexity,
especially when an admissible and consistent heuristic function is used.

### Test map
Iterations: 108
```
*********************************
*     **********************    *
*   *******   D....**********   *
*   *******       .             *
* ****************.   ***********
************.......   ********  *
*           .********************
* ********  . *******************
*********   .               *****
******      .************       *
****        .......*********    *
**      ******    . *************
******************.      ********
****      ****   ..       ***** *
*                .              *
*                s              *
*********************************
```

## Experiment algorithms with larger maps

### 300 x 300 Map

#### BFS
```
Iterations: 47186
Path length: 554
The algorithm took 0.3949906826019287 seconds to run.
```

#### Greedy
```
Iterations: 2425
Path length: 746
The algorithm took 0.023096323013305664 seconds to run.
```

#### A*
```
Iterations: 8200
Path length: 554
The algorithm took 0.08000659942626953 seconds to run.
```

### 600 x 600 Map

#### BFS
```
Iterations: 197806
Path length: 1248
The algorithm took 1.4158146381378174 seconds to run.
```

#### Greedy
```
Iterations: 9591
Path length: 1764
The algorithm took 0.08800101280212402 seconds to run.
```

#### A*
```
Iterations: 60472
Path length: 1248
The algorithm took 0.5610461235046387 seconds to run.
```

### 900 x 900 Map

#### BFS
```
Iterations: 450414
Path length: 1844
The algorithm took 3.0334599018096924 seconds to run.
```

#### Greedy
```
Iterations: 11172
Path length: 2538
The algorithm took 0.10502052307128906 seconds to run.
```

#### A*
```
Iterations: 93999
Path length: 1844
The algorithm took 0.9422404766082764 seconds to run.
```

## Conclusion
BFS finds the shortest path between the start and end points,
but it requires many more iteration steps than the greedy and A* algorithms.
This is also reflected in the time taken, which is several times longer than that of the greedy and A* algorithms.

A greedy search does not guarantee the shortest path,
but it finds a path from the start to the end point with the fewest iteration steps.
The algorithm runs very quickly, making it a good choice if you simply need a path between two points.

The A* algorithm finds the shortest path between the start and end points,
but it takes more iteration steps than the greedy search and fewer than BFS.
In terms of time, A* is faster than BFS but slower than the greedy search.