def largest_number(arr):
    largest = arr[0]
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
    return largest

arr1 = [123, 2342, 2348768768]
print(largest_number(arr1))