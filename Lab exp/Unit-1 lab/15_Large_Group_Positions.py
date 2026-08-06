def large_group_positions(s):
    result = []
    i = 0

    while i < len(s):
        j = i

        while j < len(s) and s[j] == s[i]:
            j += 1

        if j - i >= 3:
            result.append([i, j - 1])

        i = j

    return result

s = input()

print(large_group_positions(s))
