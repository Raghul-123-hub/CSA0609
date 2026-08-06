from itertools import permutations

def assignment_problem(cost):
    n = len(cost)

    minimum = float("inf")
    answer = None

    for perm in permutations(range(n)):
        total = 0

        for i in range(n):
            total += cost[i][perm[i]]

        if total < minimum:
            minimum = total
            answer = perm

    return answer, minimum

n = int(input())

cost = []

for _ in range(n):
    cost.append(list(map(int, input().split())))

assignment, total = assignment_problem(cost)

print(assignment)
print(total)
