from itertools import permutations
from math import dist

def tsp(cities):
    start = cities[0]

    minimum = float("inf")
    best = None

    for perm in permutations(cities[1:]):
        path = [start] + list(perm) + [start]

        total = 0

        for i in range(len(path) - 1):
            total += dist(path[i], path[i + 1])

        if total < minimum:
            minimum = total
            best = path

    return minimum, best

n = int(input())

cities = []

for _ in range(n):
    x, y = map(int, input().split())
    cities.append((x, y))

distance, path = tsp(cities)

print(distance)
print(path)
