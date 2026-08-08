from itertools import permutations

def tsp(matrix):
    n = len(matrix)
    best = float('inf')

    for path in permutations(range(1, n)):
        route = (0,) + path + (0,)
        cost = sum(matrix[route[i]][route[i + 1]] for i in range(n))

        best = min(best, cost)

    return best


test1 = [
    [0, 10, 15, 20],
    [10, 0, 35, 25],
    [15, 35, 0, 30],
    [20, 25, 30, 0]
]

test2 = [
    [0, 10, 10, 10],
    [10, 0, 10, 10],
    [10, 10, 0, 10],
    [10, 10, 10, 0]
]

test3 = [
    [0, 1, 2, 3],
    [1, 0, 4, 5],
    [2, 4, 0, 6],
    [3, 5, 6, 0]
]

print(tsp(test1))
print(tsp(test2))
print(tsp(test3))
