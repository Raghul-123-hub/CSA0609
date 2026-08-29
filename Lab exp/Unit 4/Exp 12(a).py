INF = float('inf')

n = 4
edges = [
    (0, 1, 3),
    (0, 2, 8),
    (0, 3, -4),
    (1, 3, 1),
    (1, 2, 4),
    (2, 0, 2),
    (3, 2, -5),
    (3, 1, 6)
]

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for u, v, w in edges:
    dist[u][v] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )

print("City 1 to City 3 =", dist[0][2])
