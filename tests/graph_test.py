import unittest

from ..algo_base.GraphCreator import GraphCreator


class GraphTest(unittest.TestCase):

    def setUp(self) -> None:
        self.Graph = GraphCreator()

        self.Graph.create_edges_from_vertexes(1, 3, 10)
        self.Graph.create_edges_from_vertexes(3, 4, 80)
        self.Graph.create_edges_from_vertexes(4, 5, 50)
        self.Graph.create_edges_from_vertexes(5, 6, 20)
        self.Graph.create_edges_from_vertexes(2, 3, 40)
        self.Graph.create_edges_from_vertexes(2, 4, 100)

    def test_graphs_vertexes(self):
        self.assertEqual([1, 3, 4, 5, 6, 2], list(self.Graph.connections.keys()))

    def test_graphs_connections(self):
        self.assertEqual(
            {1: [(3, 10)],
             3: [(1, 10), (4, 80), (2, 40)],
             4: [(3, 80), (5, 50), (2, 100)],
             5: [(4, 50), (6, 20)],
             6: [(5, 20)],
             2: [(3, 40), (4, 100)]
             },
            self.Graph.connections
        )

    def test_graph_wrong_inputs(self):
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, '1', 2, 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, '2', 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, 2, '3')
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1.5, 2, 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, 2.5, 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, 2, 3.5)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, {1}, 2, 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, {2}, 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, 2, {3})
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, [1], 2, 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, [2], 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, 2, [3])
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, (1,), 2, 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, (2,), 3)
        self.assertRaises(TypeError, self.Graph.create_edges_from_vertexes, 1, 2, (3,))
        self.assertRaises(ValueError, self.Graph.create_edges_from_vertexes, 1, 2, -3)


if __name__ == '__main__':
    unittest.main()
