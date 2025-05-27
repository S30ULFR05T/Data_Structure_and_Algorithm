def sorting_method(arr):
    n = len(arr)
    for i in range(n):
        for j in range(0, n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]

arr = [1, 97, 42, 634, 8632, 332]

sorting_method(arr)
print(arr)