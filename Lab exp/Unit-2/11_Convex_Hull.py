def orientation(p, q, r):
    return (q[1]-p[1])*(r[0]-q[0])-(q[0]-p[0])*(r[1]-q[1])

def convex_hull(points):
    points = sorted(set(points))

    if len(points) <= 1:
        return points

    lower = []

    for p in points:
        while len(lower) >= 2 and orientation(lower[-2], lower[-1], p) <= 0:
            lower.pop()
        lower.append(p)

    upper = []

    for p in reversed(points):
        while len(upper) >= 2 and orientation(upper[-2], upper[-1], p) <= 0:
            upper.pop()
        upper.append(p)

    return lower[:-1] + upper[:-1]

n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print(convex_hull(points))
