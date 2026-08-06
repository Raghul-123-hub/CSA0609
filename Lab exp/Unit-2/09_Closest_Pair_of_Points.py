from math import sqrt

def closest_pair(points):
    minimum = float("inf")
    pair = None

    for i in range(len(points)):
        for j in range(i + 1, len(points)):
            d = sqrt((points[i][0] - points[j][0]) ** 2 +
                     (points[i][1] - points[j][1]) ** 2)

            if d < minimum:
                minimum = d
                pair = (points[i], points[j])

    return pair, minimum

n = int(input())

points = []

for _ in range(n):
    x, y = map(int, input().split())
    points.append((x, y))

pair, distance = closest_pair(points)

print(pair)
print(distance)
