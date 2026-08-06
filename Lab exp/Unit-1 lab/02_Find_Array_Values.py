def find_array_values(nums1, nums2):
    answer1 = 0
    answer2 = 0

    s1 = set(nums1)
    s2 = set(nums2)

    for num in nums1:
        if num in s2:
            answer1 += 1

    for num in nums2:
        if num in s1:
            answer2 += 1

    return [answer1, answer2]

nums1 = list(map(int, input().split()))
nums2 = list(map(int, input().split()))

print(find_array_values(nums1, nums2))
