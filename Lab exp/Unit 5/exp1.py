def max_coins(piles):
    piles.sort()

    # Alice takes largest, you take second largest,
    # Bob takes smallest.
    left = 0
    right = len(piles) - 1
    result = 0

    while left < right:
        # Alice takes largest
        right -= 1

        # You take next largest
        result += piles[right]
        right -= 1

        # Bob takes smallest
        left += 1

    return result


# Test Case 1
piles = [2, 4, 1, 2, 7, 8]
print("Maximum coins:", max_coins(piles))

# Test Case 2
piles = [2, 4, 5]
print("Maximum coins:", max_coins(piles))
