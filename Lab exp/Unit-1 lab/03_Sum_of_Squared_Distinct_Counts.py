def sum_counts(nums):
    total = 0

    for i in range(len(nums)):
        s = set()
        for j in range(i, len(nums)):
            s.add(nums[j])
            total += len(s) ** 2

    return total

nums = list(map(int, input().split()))

print(sum_counts(nums))
