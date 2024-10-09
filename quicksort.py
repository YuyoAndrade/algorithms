def quicksort(n):
    if len(n) <= 1:
        return n
    left, right = [], []
    pivot = n[0]
    for i in range(1, len(n)):
        if n[i] > pivot:
            right.append(n[i])
        else:
            left.append(n[i])
    return quicksort(left) + [pivot] + quicksort(right)



print(quicksort([5, 4, 3, 2, 1, 0]))

print(quicksort([3432, 653, 12, 778, 20]))

print(quicksort([10, 7, 9, 2, 3, 4, 6, 11]))

# Time Complexity O(n^2)
# Space Complexity O(n)