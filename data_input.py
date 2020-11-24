from .algo_base.GraphCreator import GraphCreator


def data_input(filename: str):
    graph = GraphCreator()
    with open(filename, 'r') as file:
        lines = file.readlines()
        n, m = tuple(int(x) for x in lines[0].split())
        users = tuple(int(x) for x in lines[1].split())
        for line in lines[2:]:
            start, end, edge_weight = tuple(int(x) for x in line.split())
            graph.create_edges_from_vertexes(start, end, edge_weight)

    return n, m, users, graph
