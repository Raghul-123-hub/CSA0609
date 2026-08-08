def assembly_line(a1, a2, t1, t2, e1, e2, x1, x2):
    n = len(a1)

    dp1 = [0] * n
    dp2 = [0] * n

    dp1[0] = e1 + a1[0]
    dp2[0] = e2 + a2[0]

    for i in range(1, n):
        dp1[i] = min(
            dp1[i - 1] + a1[i],
            dp2[i - 1] + t2[i - 1] + a1[i]
        )

        dp2[i] = min(
            dp2[i - 1] + a2[i],
            dp1[i - 1] + t1[i - 1] + a2[i]
        )

    return min(dp1[-1] + x1, dp2[-1] + x2)


a1 = [7, 9, 3, 4, 8, 4]
a2 = [8, 5, 6, 4, 5, 7]
t1 = [2, 3, 1, 3, 4]
t2 = [2, 1, 2, 2, 1]
e1, e2 = 2, 4
x1, x2 = 3, 2

print("Minimum processing time:", assembly_line(a1, a2, t1, t2, e1, e2, x1, x2))
