from ..algo_base.GraphCreator import GraphCreator
from ..algo_base.dejkstra_algo import dejkstra
import unittest


class DejkstraTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Graph = GraphCreator()

        self.Graph.create_edges_from_vertexes(1, 3, 10)
        self.Graph.create_edges_from_vertexes(3, 4, 80)
        self.Graph.create_edges_from_vertexes(4, 5, 50)
        self.Graph.create_edges_from_vertexes(5, 6, 20)
        self.Graph.create_edges_from_vertexes(2, 3, 40)
        self.Graph.create_edges_from_vertexes(2, 4, 100)

    def test_dejkstra(self):
        self.assertRaises(ValueError, dejkstra, self.Graph, 0)
        self.assertEqual({1: 0, 3: 10, 4: 90, 5: 140, 6: 160, 2: 50},
                         dejkstra(self.Graph, 1))
        self.assertEqual({1: 50, 3: 40, 4: 100, 5: 150, 6: 170, 2: 0},
                         dejkstra(self.Graph, 2))
        self.assertEqual({1: 10, 3: 0, 4: 80, 5: 130, 6: 150, 2: 40},
                         dejkstra(self.Graph, 3))
        self.assertEqual({1: 90, 3: 80, 4: 0, 5: 50, 6: 70, 2: 100},
                         dejkstra(self.Graph, 4))
        self.assertEqual({1: 140, 3: 130, 4: 50, 5: 0, 6: 20, 2: 150},
                         dejkstra(self.Graph, 5))
        self.assertEqual({1: 160, 3: 150, 4: 70, 5: 20, 6: 0, 2: 170},
                         dejkstra(self.Graph, 6))


if __name__ == '__main__':
    unittest.main()
