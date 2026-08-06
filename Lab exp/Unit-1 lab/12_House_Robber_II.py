def rob_linear(nums):
    prev = curr = 0

    for num in nums:
        prev, curr = curr, max(curr, prev + num)

    return curr

def rob(nums):

    if len(nums) == 1:
        return nums[0]

    return max(
        rob_linear(nums[:-1]),
        rob_linear(nums[1:])
    )

nums = list(map(int, input().split()))

print(rob(nums))
