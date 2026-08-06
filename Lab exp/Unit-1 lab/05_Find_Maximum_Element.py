def find_max(arr):
    if not arr:
        return None

    maximum = arr[0]

    for num in arr:
        if num > maximum:
            maximum = num

    return maximum

arr = list(map(int, input().split()))

print(find_max(arr))
