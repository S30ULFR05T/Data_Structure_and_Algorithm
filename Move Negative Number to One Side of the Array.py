def move_negative_number (arr):
    j = 0
    n = len(arr)
    for i in range (0, n):
        if arr[i] < 0:
            temp = arr[i]
            arr[i] = arr[j]
            arr[j] = temp
            j = j + 1

    return arr

arr = [4, -1, 2, -90, 2]
print(move_negative_number(arr))

arr = [1, 2, -4, -3, -90, 2, 50, 38, -9, 1]
print(move_negative_number(arr))