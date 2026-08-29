INF = float('inf')

edges = [
    ("B", "A", 2),
    ("A", "C", 3),
    ("C", "D", 1),
    ("D", "A", 6),
    ("C", "B", 7)
]

nodes = ["A", "B", "C", "D"]
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

print("C to A =", dist[nodes.index("C")][nodes.index("A")])
