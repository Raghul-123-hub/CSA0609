class DSU:
    def __init__(self, n):
        self.parent = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, a, b):
        a = self.find(a)
        b = self.find(b)

        if a == b:
            return False

        if self.rank[a] < self.rank[b]:
            self.parent[a] = b
        elif self.rank[a] > self.rank[b]:
            self.parent[b] = a
        else:
            self.parent[b] = a
            self.rank[a] += 1

        return True


def kruskal_mst(n, edges, banned_edge=None):
    edges = sorted(edges, key=lambda x: x[2])

    dsu = DSU(n)

    mst = []
    total = 0

    for edge in edges:

        if banned_edge is not None and edge == banned_edge:
            continue

        u, v, w = edge

        if dsu.union(u, v):
            mst.append(edge)
            total += w

            if len(mst) == n - 1:
                break

    # Graph is disconnected
    if len(mst) != n - 1:
        return None, float('inf')

    return mst, total


def check_unique_mst(n, edges, given_mst):
    # Find weight of given MST
    given_weight = sum(edge[2] for edge in given_mst)

    # Check by removing each MST edge
    for banned in given_mst:

        alternative_mst, alternative_weight = kruskal_mst(
            n,
            edges,
            banned
        )

        if alternative_weight == given_weight:
            return False, alternative_mst, alternative_weight

    return True, None, given_weight


# -----------------------------
# Test Case 1
# -----------------------------

n = 4

edges = [
    (0, 1, 10),
    (0, 2, 6),
    (0, 3, 5),
    (1, 3, 15),
    (2, 3, 4)
]

given_mst = [
    (2, 3, 4),
    (0, 3, 5),
    (0, 1, 10)
]

unique, alternative, weight = check_unique_mst(
    n,
    edges,
    given_mst
)

print("Is the given MST unique?", unique)

if not unique:
    print("Another possible MST:", alternative)
    print("Total weight:", weight)


# -----------------------------
# Test Case 2
# -----------------------------

n = 5

edges = [
    (0, 1, 1),
    (0, 2, 1),
    (1, 3, 2),
    (2, 3, 2),
    (3, 4, 3),
    (4, 2, 3)
]

given_mst = [
    (0, 1, 1),
    (0, 2, 1),
    (1, 3, 2),
    (3, 4, 3)
]

unique, alternative, weight = check_unique_mst(
    n,
    edges,
    given_mst
)

print("Is the given MST unique?", unique)

if not unique:
    print("Another possible MST:", alternative)
    print("Total weight:", weight)
