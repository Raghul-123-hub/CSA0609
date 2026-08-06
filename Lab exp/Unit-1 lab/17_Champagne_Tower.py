def champagne_tower(poured, query_row, query_glass):
    dp = [[0.0] * 101 for _ in range(101)]

    dp[0][0] = poured

    for i in range(100):
        for j in range(i + 1):
            overflow = max(0.0, (dp[i][j] - 1) / 2)

            dp[i + 1][j] += overflow
            dp[i + 1][j + 1] += overflow

    return min(1, dp[query_row][query_glass])

poured = int(input())
query_row = int(input())
query_glass = int(input())

print(champagne_tower(poured, query_row, query_glass))
