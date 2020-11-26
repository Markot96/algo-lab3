from .algo_base.dejkstra_algo import dejkstra
from .data_input import data_input
from .data_output import data_output


def main():
    n, m, users, graph = data_input('gamsrv.in')
    min_max_latency = None
    for vertex_id in graph.connections:
        if vertex_id not in users:
            current_latencies = dejkstra(graph, vertex_id)
            current_max_latency = max([current_latencies[user] for user in users])
            if min_max_latency is None:
                min_max_latency = current_max_latency
            elif current_max_latency < min_max_latency:
                min_max_latency = current_max_latency

    data_output('gamsrv.out', min_max_latency)

    return min_max_latency


if __name__ == '__main__':
    print(main())

