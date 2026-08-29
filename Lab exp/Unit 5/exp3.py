def min_coins_to_add(coins, target):
    coins.sort()

    reachable = 1
    index = 0
    added = 0

    while reachable <= target:
        if index < len(coins) and coins[index] <= reachable:
            reachable += coins[index]
            index += 1
        else:
            # Add a coin with value equal to reachable
            reachable += reachable
            added += 1

    return added


# Test Case 1
coins = [1, 4, 10]
target = 19
print("Minimum coins to add:", min_coins_to_add(coins, target))

# Test Case 2
coins = [1, 4, 10, 5, 7, 19]
target = 19
print("Minimum coins to add:", min_coins_to_add(coins, target))
