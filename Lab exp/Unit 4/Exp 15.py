def optimal_bst(keys, freq):
    n = len(keys)

    cost = [[0] * n for _ in range(n)]
    root = [[0] * n for _ in range(n)]

    for i in range(n):
        cost[i][i] = freq[i]
        root[i][i] = i

    for length in range(2, n + 1):
        for i in range(n - length + 1):
            j = i + length - 1
            total = sum(freq[i:j + 1])
            cost[i][j] = float('inf')

            for r in range(i, j + 1):
                left = cost[i][r - 1] if r > i else 0
                right = cost[r + 1][j] if r < j else 0

                value = left + right + total

                if value < cost[i][j]:
                    cost[i][j] = value
                    root[i][j] = r

    print("Cost Matrix:")
    for row in cost:
        print(row)

    print("\nRoot Matrix:")
    for row in root:
        print(row)

    print("\nMinimum Cost:", cost[0][n - 1])


keys = ["A", "B", "C", "D"]
freq = [0.1, 0.2, 0.4, 0.3]

optimal_bst(keys, freq)
