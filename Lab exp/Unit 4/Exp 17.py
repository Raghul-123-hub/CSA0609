from collections import deque

def cat_mouse_game(graph):
    n = len(graph)

    DRAW = 0
    MOUSE = 1
    CAT = 2

    degree = [[[0] * 2 for _ in range(n)] for _ in range(n)]
    color = [[[DRAW] * 2 for _ in range(n)] for _ in range(n)]

    queue = deque()

    for m in range(n):
        for c in range(n):
            degree[m][c][0] = len(graph[m])
            degree[m][c][1] = sum(1 for x in graph[c] if x != 0)

    for c in range(1, n):
        color[0][c][0] = MOUSE
        queue.append((0, c, 0, MOUSE))

    for c in range(1, n):
        color[c][c][0] = CAT
        color[c][c][1] = CAT

        queue.append((c, c, 0, CAT))
        queue.append((c, c, 1, CAT))

    while queue:
        m, c, turn, result = queue.popleft()

        for pm, pc, pturn in predecessors(graph, m, c, turn):
            if color[pm][pc][pturn] != DRAW:
                continue

            if (pturn == 0 and result == MOUSE) or \
               (pturn == 1 and result == CAT):
                color[pm][pc][pturn] = result
                queue.append((pm, pc, pturn, result))
            else:
                degree[pm][pc][pturn] -= 1

                if degree[pm][pc][pturn] == 0:
                    opposite = CAT if pturn == 0 else MOUSE
                    color[pm][pc][pturn] = opposite
                    queue.append((pm, pc, pturn, opposite))

    return color[1][2][0]


def predecessors(graph, m, c, turn):
    if turn == 0:
        for pc in graph[c]:
            if pc != 0:
                yield m, pc, 1
    else:
        for pm in graph[m]:
            yield pm, c, 0


graph1 = [
    [2, 5],
    [3],
    [0, 4, 5],
    [1, 4, 5],
    [2, 3],
    [0, 2, 3]
]

graph2 = [
    [1, 3],
    [0],
    [3],
    [0, 2]
]

print("Example 1:", cat_mouse_game(graph1))
print("Example 2:", cat_mouse_game(graph2))
