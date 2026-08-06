def find_kth_positive(arr, k):
    current = 1
    i = 0

    while k > 0:
        if i < len(arr) and arr[i] == current:
            i += 1
        else:
            k -= 1
            if k == 0:
                return current
        current += 1

arr = list(map(int, input().split()))
k = int(input())

print(find_kth_positive(arr, k))
