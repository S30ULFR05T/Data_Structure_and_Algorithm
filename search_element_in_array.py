arr = [1, 2, 3, 5, 6, 12, 99, 32, 41, 901, 342]
n = len(arr)
k = 1
ans = -1

for i in range(n):
    if arr[i] == k:
        ans = i
        break

print("The element is present in ", ans)