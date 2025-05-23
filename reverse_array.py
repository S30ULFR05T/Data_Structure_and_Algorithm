def reverse_array(arr):
    n = len(arr)
    initial = 0
    final = n-1

    while initial < final:
        arr[initial], arr[final] = arr[final], arr[initial]
        initial += 1
        final -= 1

arr1 = [1, 3, 2, 6, 98, 5]
reverse_array(arr1)
print(f"Reversed Array --> {arr1}")