INF = float('inf')

def floyd_warshall(n, edges):
    dist = [[INF] * n for _ in range(n)]

    for i in range(n):
        dist[i][i] = 0

    for u, v, w in edges:
        dist[u][v] = w
        dist[v][u] = w

    print("Before Floyd-Warshall:")
    for row in dist:
        print(row)

    for k in range(n):
        for i in range(n):
            for j in range(n):
                dist[i][j] = min(
                    dist[i][j],
                    dist[i][k] + dist[k][j]
                )

    print("\nAfter Floyd-Warshall:")
    for row in dist:
        print(row)

    return dist


edges = [
    [0, 1, 3],
    [1, 2, 1],
    [1, 3, 4],
    [2, 3, 1]
]

dist = floyd_warshall(4, edges)

threshold = 4

for i in range(4):
    count = sum(
        1 for j in range(4)
        if i != j and dist[i][j] <= threshold
    )
    print("City", i, "neighbors:", count)
