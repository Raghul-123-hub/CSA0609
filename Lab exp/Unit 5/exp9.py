def maximum_weight(weights, max_capacity):
    weights.sort(reverse=True)

    total = 0

    for weight in weights:
        if total + weight <= max_capacity:
            total += weight

        if total == max_capacity:
            break

    return total


# Test Case 1
weights = [10, 20, 30, 40, 50]
capacity = 60

print("Maximum weight:", maximum_weight(weights, capacity))


# Test Case 2
weights = [5, 10, 15, 20, 25, 30]
capacity = 50

print("Maximum weight:", maximum_weight(weights, capacity))
