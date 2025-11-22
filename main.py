
## main.py
```python
import heapq
from collections import deque


def route_planner(graph, start, goal, weighted):
    """
    Plan a route between start and goal.

    If weighted is False:
        - graph: dict node -> list of neighbor nodes (unweighted).
        - Use BFS to find a path with the fewest edges.
        - Return (path, steps) where steps = number of edges.

    If weighted is True:
        - graph: dict node -> list of (neighbor, weight) pairs (positive weights).
        - Use Dijkstra to find a path with the smallest total weight.
        - Return (path, total_cost).

    In both cases:
        - If start or goal not in graph, or no path exists, return ([], None).
    """
    # TODO Step 1–3: Understand the two modes and write down inputs/outputs.
    # TODO Step 4: Plan how to choose BFS or Dijkstra based on the `weighted` flag.
    # TODO Step 5: Write pseudocode for the BFS branch and the Dijkstra branch.
    # TODO Step 6: Implement helper functions (if you wish) and call them here.
    # TODO Step 7: Test both unweighted and weighted graphs, including no-path cases.
    # TODO Step 8: Reflect why BFS is used for unweighted and Dijkstra for weighted.

    raise NotImplementedError("route_planner is not implemented yet")


if __name__ == "__main__":
    # Optional manual tests can go here
    pass
