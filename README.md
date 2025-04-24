# BFS Traversal CLI

This project implements **Breadth-First Search (BFS)** on an undirected graph using a plain text edge list as input. The program reads the graph from a file, performs BFS from a specified start node, and prints nodes visited at each iteration along with their parent relationships.

Designed for large graphs and tested for command-line execution on Unix-based environments like **Zeus**.

---

## Features
- Efficient BFS using adjacency list and `deque`
- Accepts graph input as an edge list from a file
- Tracks and prints visited nodes per iteration
- Tracks parent relationships for traversal
- Outputs final BFS traversal order (1 node per line)
- Supports large-scale graphs and command-line execution
- Includes complete unit tests using `unittest`

## Requirements

- Python 3.6 or higher
- Works on Linux, macOS, Windows, and Zeus

## Target of unit tests for BFS
1. Traversing the graph correctly from a given start node
2. Visiting each node exactly once (no duplicates)
3. Respecting adjacency list structure (undirected edges)
4. Using sorted() on neighbors (for consistent traversal order)
5. Returning the correct list of visited nodes in BFS order

. Implement the functions:
- read_graph(file_name)
- print_final_traversal(order)
- print_iteration_info(visited_iteration, parent)
- bfs(graph, start_node)
- main()

2. Implement unit tests for BFS:
- Basic BFS: small connected graph
- Graph with cycles: Ensure BFS avoids revisiting nodes
- Disconnected graph: Only reachable nodes from start_node are visited
- Single node: One node with no edges
- Multiple components: Graph sorting gives consistent traversal order
- Empty graph: No nodes
- Start node not in graph: Should raise error in main(), but now skip it


