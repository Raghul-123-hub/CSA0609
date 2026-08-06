from functools import lru_cache

def find_paths(m, n, N, i, j):

    @lru_cache(None)
    def dfs(x, y, steps):
        if x < 0 or x >= m or y < 0 or y >= n:
            return 1

        if steps == 0:
            return 0

        return (
            dfs(x + 1, y, steps - 1) +
            dfs(x - 1, y, steps - 1) +
            dfs(x, y + 1, steps - 1) +
            dfs(x, y - 1, steps - 1)
        )

    return dfs(i, j, N)

m = int(input())
n = int(input())
N = int(input())
i = int(input())
j = int(input())

print(find_paths(m, n, N, i, j))
