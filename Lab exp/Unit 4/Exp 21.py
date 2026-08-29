def find_the_city(n, edges, distanceThreshold):
    INF = float('inf')

    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    answer = -1
    minimum = INF

    for i in range(n):
        count = sum(
            1 for j in range(n)
            if i != j and dist[i][j] <= distanceThreshold
        )

        if count <= minimum:
            minimum = count
            answer = i

    return answer


edges1 = [
    [0, 1, 3],
    [1, 2, 1],
    [1, 3, 4],
    [2, 3, 1]
]

edges2 = [
    [0, 1, 2],
    [0, 4, 8],
    [1, 2, 3],
    [1, 4, 2],
    [2, 3, 1],
    [3, 4, 1]
]

print(find_the_city(4, edges1, 4))
print(find_the_city(5, edges2, 2))
