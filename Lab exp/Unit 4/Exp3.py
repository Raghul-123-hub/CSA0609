def three_assembly_lines(lines, transfer, dependencies):
    n = len(lines[0])
    k = len(lines)

    dp = [[float('inf')] * n for _ in range(k)]

    for line in range(k):
        dp[line][0] = lines[line][0]

    for station in range(1, n):
        for line in range(k):
            for prev in range(k):
                dp[line][station] = min(
                    dp[line][station],
                    dp[prev][station - 1] +
                    transfer[prev][line] +
                    lines[line][station]
                )

    return min(dp[line][n - 1] for line in range(k))


lines = [
    [5, 9, 3],
    [6, 8, 4],
    [7, 6, 5]
]

transfer = [
    [0, 2, 3],
    [2, 0, 4],
    [3, 4, 0]
]

dependencies = [(0, 1), (1, 2)]

print("Minimum production time:",
      three_assembly_lines(lines, transfer, dependencies))
