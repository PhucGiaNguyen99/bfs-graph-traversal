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