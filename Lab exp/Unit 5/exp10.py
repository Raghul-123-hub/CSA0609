def minimum_containers(weights, capacity):
    containers = 1
    current_weight = 0

    for weight in weights:

        if current_weight + weight <= capacity:
            current_weight += weight

        else:
            containers += 1
            current_weight = weight

    return containers


# Test Case 1
weights = [5, 10, 15, 20, 25, 30, 35]
capacity = 50

print("Minimum containers:", minimum_containers(
    weights, capacity
))


# Test Case 2
weights = [10, 20, 30, 40, 50, 60, 70, 80]
capacity = 100

print("Minimum containers:", minimum_containers(
    weights, capacity
))
