def find_duplicate(arr):
    n = len(arr)

    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]

    # After sorting, check for duplicates
    for i in range(1, n):
        if arr[i] == arr[i - 1]:
            return arr[i]  # Found duplicate

    return None  # No duplicates found


arr = [1, 97, 42, 634, 8632, 42]
duplicate = find_duplicate(arr)
print("Sorted array:", arr)
print("Duplicate element:", duplicate)
