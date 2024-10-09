def minSubArrayLen(target: int, nums) -> int:
    if len(nums) == 0:
        return 0
    elif len(nums) == 1:
        return 1 if nums[0] >= target else 0

    suma = 0
    arr = []
    min_arr = 999999
    i, j = 0, 0

    while j < len(nums):
        if suma >= target:
            min_arr = min(min_arr, len(arr))
            i += 1
            suma -= arr[0]
            arr.pop(0)
        else:
            arr.append(nums[j])
            j += 1
            suma += arr[-1]
    while suma - arr[0] >= target:
        suma -= arr[0]
        arr.pop(0)
        min_arr = min(min_arr, len(arr))

    if suma >= target:
        return min(min_arr, len(arr))

    return min_arr if min_arr != 999999 else 0


print(minSubArrayLen(7, [2, 3, 1, 2, 4, 3]))
print(minSubArrayLen(11, [1, 2, 3, 4, 5]))
print(minSubArrayLen(15, [1, 2, 3, 4, 5]))
