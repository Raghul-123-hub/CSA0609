from itertools import permutations

cities = ["A", "B", "C", "D", "E"]

dist = {
    "AB": 10, "AC": 15, "AD": 20, "AE": 25,
    "BC": 35, "BD": 25, "BE": 30,
    "CD": 30, "CE": 20,
    "DE": 15
}

def get_distance(a, b):
    return dist.get(a + b, dist.get(b + a))


best_distance = float('inf')
best_route = None

for p in permutations(cities[1:]):
    route = ["A"] + list(p) + ["A"]
    total = 0

    for i in range(len(route) - 1):
        total += get_distance(route[i], route[i + 1])

    if total < best_distance:
        best_distance = total
        best_route = route

print("Shortest Route:", " -> ".join(best_route))
print("Minimum Distance:", best_distance)
