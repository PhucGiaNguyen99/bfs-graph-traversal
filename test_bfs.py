import unittest
from collections import defaultdict
from bfs import bfs

class TestBfS(unittest.TestCase):

    def test_basic_bfs(self):
        graph = {
            1: [2, 3],
            2: [1, 4], 
            3: [1],
            4: [2]
        }

        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_bfs_with_cycle(self):
        graph = {
            1: [2],
            2: [1, 3, 4],
            3: [2, 4],
            4: [2, 3]
        }
        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_disconnected_graph(self):
        graph = {
            1: [2],
            2: [1],
            3: [4],
            4: [3]
        }
        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2])
    
    def test_single_node(self):
        graph = {
            5: []
        }
        result = bfs(graph, 5)
        self.assertEqual(result, [5])
    
    def test_multiple_components(self):
        graph = {
            1: [2],
            2: [1],
            3: [4, 5],
            4: [3],
            5: [3]
        }
        result = bfs(graph, 3)
        self.assertEqual(result, [3, 4, 5])

    def test_unordered_adjacency(self):
        graph = {
            1: [3, 2],
            2: [1],
            3: [1, 4],
            4: [3]
        }
        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2, 3, 4])
    
    def test_empty_graph(self):
        graph = {}
        with self.assertRaises(KeyError):
            bfs(graph, 1)
    
    def test_bfs_with_self_loop(self):
        """
        Node has an edge to itself. BFS should not get stuck or revisit.
        """
        graph = {
            1: [1, 2],
            2: [1]
        }
        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2])
        self.assertEqual(len(result), 2)
    
    def test_bfs_multiple_paths(self):
        """
        Multiple paths to reach a node. It should still visit only once.
        """
        graph = {
            1: [2, 3],
            2: [1, 4],
            3: [1, 4],
            4: [2, 3]
        }
        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(len(set(result)), 4)  # Ensure no duplicates
    
    def test_bfs_tree_structure(self):
        """
        BFS on a binary tree-shaped graph.
        """
        graph = {
            1: [2, 3],
            2: [1, 4, 5],
            3: [1],
            4: [2],
            5: [2]
        }
        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2, 3, 4, 5])

    def test_bfs_grid_structure(self):
        """
        Simulates a 2x2 grid:
        1 - 2
        |   |
        3 - 4
        """
        graph = {
            1: [2, 3],
            2: [1, 4],
            3: [1, 4],
            4: [2, 3]
        }
        result = bfs(graph, 1)
        self.assertEqual(result, [1, 2, 3, 4])
        self.assertEqual(len(result), 4)
    
    def test_bfs_length_check(self):
        """
        BFS result should have the correct number of reachable nodes.
        """
        graph = {
            10: [20, 30],
            20: [10],
            30: [10, 40],
            40: [30],
            99: []  # disconnected
        }
        result = bfs(graph, 10)
        self.assertEqual(len(result), 4)  # Should not include node 99