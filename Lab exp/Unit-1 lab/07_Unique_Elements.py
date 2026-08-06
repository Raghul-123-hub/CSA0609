def unique_elements(arr):
    result = []

    for num in arr:
        if num not in result:
            result.append(num)

    return result

arr = list(map(int, input().split()))

print(unique_elements(arr))
