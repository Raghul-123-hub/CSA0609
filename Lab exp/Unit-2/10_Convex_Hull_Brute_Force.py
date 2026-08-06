def orientation(p, q, r):
    return (q[0] - p[0]) * (r[1] - p[1]) - (q[1] - p[1]) * (r[0] - p[0])

def convex_hull(points):
    n = len(points)
    hull = []

    for i in range(n):
        for j in range(i + 1, n):
            left = right = 0

            for k in range(n):
                if k == i or k == j:
                    continue

                val = orientation(points[i], points[j], points[k])

                if val > 0:
                    left += 1
                elif val < 0:
                    right += 1

            if left == 0 or right == 0:
                if points[i] not in hull:
                    hull.append(points[i])
                if points[j] not in hull:
                    hull.append(points[j])

    return hull

n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

print(convex_hull(points))
