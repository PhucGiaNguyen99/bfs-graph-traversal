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