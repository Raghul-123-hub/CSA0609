INF = float('inf')

edges = [
    ("C", "A", 2),
    ("A", "B", 4),
    ("B", "C", 1),
    ("B", "E", 6),
    ("E", "A", 1),
    ("A", "D", 5),
    ("D", "E", 2),
    ("E", "D", 4),
    ("D", "C", 1),
    ("C", "D", 3)
]

nodes = ["A", "B", "C", "D", "E"]
n = len(nodes)

dist = [[INF] * n for _ in range(n)]

for i in range(n):
    dist[i][i] = 0

for u, v, w in edges:
    dist[nodes.index(u)][nodes.index(v)] = w

for k in range(n):
    for i in range(n):
        for j in range(n):
            dist[i][j] = min(
                dist[i][j],
                dist[i][k] + dist[k][j]
            )

print("E to C =", dist[nodes.index("E")][nodes.index("C")])
