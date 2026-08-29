INF = float('inf')

routers = ["A", "B", "C", "D", "E", "F"]
n = 6

edges = [
    ("A", "B", 1),
    ("A", "C", 5),
    ("B", "C", 2),
    ("B", "D", 1),
    ("C", "E", 3),
    ("D", "E", 1),
    ("D", "F", 6),
    ("E", "F", 2)
]

def floyd(edges):
    d = [[INF] * n for _ in range(n)]

    for i in range(n):
        d[i][i] = 0

    for u, v, w in edges:
        a = routers.index(u)
        b = routers.index(v)
        d[a][b] = w
        d[b][a] = w

    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k] + d[k][j])

    return d


before = floyd(edges)

failed_edges = [
    e for e in edges
    if not (e[0] == "B" and e[1] == "D")
]

after = floyd(failed_edges)

print("Before link failure A to F:", before[0][5])
print("After link failure A to F:", after[0][5])
