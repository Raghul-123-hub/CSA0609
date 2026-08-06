from itertools import combinations

def knapsack(weights, values, capacity):
    n = len(weights)

    best_value = 0
    best_items = []

    for r in range(n + 1):
        for comb in combinations(range(n), r):
            weight = sum(weights[i] for i in comb)
            value = sum(values[i] for i in comb)

            if weight <= capacity and value > best_value:
                best_value = value
                best_items = list(comb)

    return best_items, best_value

weights = list(map(int, input().split()))
values = list(map(int, input().split()))
capacity = int(input())

items, value = knapsack(weights, values, capacity)

print(items)
print(value)
