def sorting_method(arr, k):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    return arr[k - 1]

arr = [129234, 249, 382, 972, 2942]
k = 5
print(sorting_method(arr, k))


