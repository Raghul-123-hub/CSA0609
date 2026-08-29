def num_good_pairs(nums):
    frequency = {}
    count = 0

    for num in nums:
        if num in frequency:
            count += frequency[num]

        frequency[num] = frequency.get(num, 0) + 1

    return count


print(num_good_pairs([1, 2, 3, 1, 1, 3]))
print(num_good_pairs([1, 1, 1, 1]))
