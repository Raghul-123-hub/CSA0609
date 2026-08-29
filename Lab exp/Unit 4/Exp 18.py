import heapq

def max_probability(n, edges, succProb, start, end):
    graph = [[] for _ in range(n)]

    for (u, v), p in zip(edges, succProb):
        graph[u].append((v, p))
        graph[v].append((u, p))

    probability = [0.0] * n
    probability[start] = 1.0

    pq = [(-1.0, start)]

    while pq:
        neg_prob, node = heapq.heappop(pq)
        prob = -neg_prob

        if node == end:
            return prob

        if prob < probability[node]:
            continue

        for neighbor, edge_prob in graph[node]:
            new_prob = prob * edge_prob

            if new_prob > probability[neighbor]:
                probability[neighbor] = new_prob
                heapq.heappush(pq, (-new_prob, neighbor))

    return 0.0


edges = [[0, 1], [1, 2], [0, 2]]

print(max_probability(
    3, edges, [0.5, 0.5, 0.2], 0, 2
))

print(max_probability(
    3, edges, [0.5, 0.5, 0.3], 0, 2
))
