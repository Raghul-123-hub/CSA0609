def dijkstra_matrix(graph, source):
    n = len(graph)

    INF = float('inf')

    distance = [INF] * n
    visited = [False] * n

    distance[source] = 0

    for _ in range(n):

        # Find unvisited vertex with minimum distance
        u = -1

        for i in range(n):
            if not visited[i] and (u == -1 or distance[i] < distance[u]):
                u = i

        if u == -1 or distance[u] == INF:
            break

        visited[u] = True

        # Relax adjacent vertices
        for v in range(n):
            if graph[u][v] != INF and not visited[v]:
                new_distance = distance[u] + graph[u][v]

                if new_distance < distance[v]:
                    distance[v] = new_distance

    return distance


# Test Case 1
INF = float('inf')

graph = [
    [0, 10, 3, INF, INF],
    [INF, 0, 1, 2, INF],
    [INF, 4, 0, 8, 2],
    [INF, INF, INF, 0, 7],
    [INF, INF, INF, 9, 0]
]

source = 0

print("Shortest distances:", dijkstra_matrix(graph, source))


# Test Case 2
graph = [
    [0, 5, INF, 10],
    [INF, 0, 3, INF],
    [INF, INF, 0, 1],
    [INF, INF, INF, 0]
]

source = 0

print("Shortest distances:", dijkstra_matrix(graph, source))
