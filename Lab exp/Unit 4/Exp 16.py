def obst(keys, freq):
    n = len(keys)

    dp = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    for i in range(n):
        dp[i][i] = freq[i]
        root[i][i] = i

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = sum(freq[i:j + 1])
            dp[i][j] = float('inf')

            for r in range(i, j + 1):
                left = dp[i][r - 1] if r > i else 0
                right = dp[r + 1][j] if r < j else 0

                value = left + right + total

                if value < dp[i][j]:
                    dp[i][j] = value
                    root[i][j] = r

    print("Cost Matrix:")
    for row in dp:
        print(row)

    print("\nRoot Matrix:")
    for row in root:
        print(row)

    print("\nMinimum Cost:", dp[0][n - 1])


keys = [10, 12, 16, 21]
freq = [4, 2, 6, 3]

obst(keys, freq)
