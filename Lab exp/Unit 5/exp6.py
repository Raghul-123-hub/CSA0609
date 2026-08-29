import heapq


def dijkstra_edge_list(n, edges, source, target):
    graph = [[] for _ in range(n)]

    # Build adjacency list
    for u, v, w in edges:
        graph[u].append((v, w))

    INF = float('inf')
    distance = [INF] * n

    distance[source] = 0

    priority_queue = [(0, source)]

    while priority_queue:

        current_distance, u = heapq.heappop(priority_queue)

        if current_distance > distance[u]:
            continue

        if u == target:
            return current_distance

        for v, weight in graph[u]:
            new_distance = current_distance + weight

            if new_distance < distance[v]:
                distance[v] = new_distance
                heapq.heappush(
                    priority_queue,
                    (new_distance, v)
                )

    return distance[target]


# Test Case 1
n = 6

edges = [
    (0, 1, 7),
    (0, 2, 9),
    (0, 5, 14),
    (1, 2, 10),
    (1, 3, 15),
    (2, 3, 11),
    (2, 5, 2),
    (3, 4, 6),
    (4, 5, 9)
]

print("Shortest path:", dijkstra_edge_list(
    n, edges, 0, 4
))


# Test Case 2
n = 5

edges = [
    (0, 1, 10),
    (0, 4, 3),
    (1, 2, 2),
    (1, 4, 4),
    (2, 3, 9),
    (3, 2, 7),
    (4, 1, 1),
    (4, 2, 8),
    (4, 3, 2)
]

print("Shortest path:", dijkstra_edge_list(
    n, edges, 0, 3
))
