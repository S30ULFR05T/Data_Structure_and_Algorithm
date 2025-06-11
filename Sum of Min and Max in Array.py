def sum_min_max(arr):
    n = len(arr)

    if n == 1:
        return arr[0]

    if arr[0] > arr[1]:
        max_element = arr[0]
        min_element = arr[1]

        print("if condition - max element", arr[0])
        print("if condition - min element", arr[1])

    else:
        max_element = arr[1]
        min_element = arr[0]

        print("else condition - max element", arr[1])
        print("else condition - min element", arr[0])

    for i in range(2, n):
        if arr[i] > max_element:
            max_element = arr[i]

            print("for if condition - max element", arr[i])

        elif arr[i] < min_element:
            min_element = arr[i]

            print("for else condition - min element", arr[i])

    return max_element, min_element, max_element + min_element
    #remove the max element and min element for just printing sum of max and min

arr = [-4, -1, 2, 90, 2]
print(sum_min_max(arr))
