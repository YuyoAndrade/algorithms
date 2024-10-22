def merge(left, right):
    sorted = []
    i, j = 0, 0
    while len(left) > i and len(right) > j:
        if left[i] <= right[j]:
            sorted.append(left[i])
            i += 1
        else:
            sorted.append(right[j])
            j += 1
    if len(left) > i:
        sorted += left[i:]
    if len(right) > j:
        sorted += right[j:]
    return sorted


def merge_sort(n):
    if len(n) <= 1:
        return n
    mid = len(n) // 2
    left = merge_sort(n[:mid])
    right = merge_sort(n[mid:])
    return merge(left, right)


nums = [4, 2, 1, 8, 7, 9, 5, 7, 7, 0]

sorted = merge_sort(nums)

print(sorted)
