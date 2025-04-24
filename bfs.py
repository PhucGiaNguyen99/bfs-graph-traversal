import sys
from collections import deque

def read_graph(file_name):
    """
    Reads an undirected graph from a text file and returns it as an adjacency list. 
    Each line of the input file should contain two integers representing their edge.

    Args:
        file_name (str): Path to the graph input file.
    
    Returns:
        dict: Adjacency list representation of the graph.
    """
    graph = {}

    with open(file_name, 'r') as file:
        for line in file:
            if line.strip():
                node1, node2 = map(int, line.strip().split())

                # Initialize adjacency lists if not already present
                if node1 not in graph:
                    graph[node1] = []
                if node2 not in graph:
                    graph[node2] = []

                # Add edge (both directions for undirected graph)
                graph[node1].append(node2)
                graph[node2].append(node1)

    return graph


def print_final_traversal(order):
    """
    Prints the final BFS traversal order, one node per line.

    Args:
        order (list): List of nodes in the order they were visited.
    """
    print("\nBFS Traversal Order:")
    for node in order:
        print(node)


def print_iteration_info(visited_iteration, parent):
    """
    Prints the list of nodes visited in the current BFS iteration
    and the current state of the parent dictionary.

    Args:
        visited_iteration (list): List of nodes visited in this BFS level.
        parent (dict): Dictionary mapping each node to its parent.
    """
    print(f"Visited this iteration: {' '.join(map(str, visited_iteration))}")
    print("Parent array:", ' '.join(f"{node}:{parent[node]}" for node in sorted(parent)))


def bfs(graph, start_node):
    """
    Performs Breadth-First Search (BFS) on a graph starting from a specified node.

    Args:
        graph (dict): Adjacency list of the graph.
        start_node (int): Node to begin the BFS traversal from.

    Returns:
        list: Nodes in the order they were visited in BFS.
    """
    visited = set()           # Tracks visited nodes
    parent = {}               # Tracks parent of each node
    queue = deque()           # Queue for BFS
    traversal_order = []      # Final BFS traversal order

    # Initialize BFS with the start node
    visited.add(start_node)
    parent[start_node] = -1   # Root node has no parent
    queue.append(start_node)

    while queue:
        level_size = len(queue)       # Number of nodes in current level
        visited_iteration = []        # Nodes visited in this iteration

        for _ in range(level_size):
            current = queue.popleft() # Dequeue the next node
            traversal_order.append(current)

            # Traverse all neighbors of the current node
            for neighbor in sorted(graph[current]):
                if neighbor not in visited:
                    visited.add(neighbor)
                    parent[neighbor] = current
                    queue.append(neighbor)
                    visited_iteration.append(neighbor)

        # Print the result of this level (iteration)
        print_iteration_info(visited_iteration, parent)

    return traversal_order


def main():
    """
    Main function that parses command-line arguments,
    reads the input graph, and initiates BFS traversal.
    """
    if len(sys.argv) != 3:
        print("Usage: python bfs.py <input_file> <start_node>")
        sys.exit(1)

    input_file = sys.argv[1]

    try:
        start_node = int(sys.argv[2])
    except ValueError:
        print("Start node must be an integer.")
        sys.exit(1)

    # Read the graph from file
    graph = read_graph(input_file)

    if start_node not in graph:
        print(f"Start node {start_node} not found in the graph.")
        sys.exit(1)

    # Run BFS and print the final traversal
    traversal_order = bfs(graph, start_node)
    print_final_traversal(traversal_order)

if __name__ == "__main__":
    main()