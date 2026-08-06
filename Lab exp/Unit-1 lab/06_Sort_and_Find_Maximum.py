def sort_and_find_max(arr):
    if len(arr) == 0:
        return None

    for i in range(len(arr)):
        for j in range(i + 1, len(arr)):
            if arr[i] > arr[j]:
                arr[i], arr[j] = arr[j], arr[i]

    return arr[-1]

arr = list(map(int, input().split()))

print(sort_and_find_max(arr))
