def binary_search(arr, key):
    arr.sort()

    low = 0
    high = len(arr) - 1

    while low <= high:
        mid = (low + high) // 2

        if arr[mid] == key:
            return mid

        elif arr[mid] < key:
            low = mid + 1

        else:
            high = mid - 1

    return -1

arr = list(map(int, input().split()))
key = int(input())

result = binary_search(arr, key)

if result != -1:
    print(result)
else:
    print("Not Found")
