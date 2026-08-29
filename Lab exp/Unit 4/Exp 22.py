import heapq

def network_delay_time(times, n, k):
    graph = [[] for _ in range(n + 1)]

    for u, v, w in times:
        graph[u].append((v, w))

    distance = [float('inf')] * (n + 1)
    distance[k] = 0

    pq = [(0, k)]

    while pq:
        current_time, node = heapq.heappop(pq)

        if current_time > distance[node]:
            continue

        for neighbor, weight in graph[node]:
            new_time = current_time + weight

            if new_time < distance[neighbor]:
                distance[neighbor] = new_time
                heapq.heappush(pq, (new_time, neighbor))

    result = max(distance[1:])

    return -1 if result == float('inf') else result


print(network_delay_time(
    [[2, 1, 1], [2, 3, 1], [3, 4, 1]],
    4,
    2
))

print(network_delay_time(
    [[1, 2, 1]],
    2,
    1
))

print(network_delay_time(
    [[1, 2, 1]],
    2,
    2
))
