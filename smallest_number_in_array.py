def smallest_number(arr):
    smallest = arr[0]
    for i in range(len(arr)):
        if arr[i] < smallest:
            smallest = arr[i]
    return smallest

arr1 = [123, 2342, 234]
print(smallest_number(arr1))