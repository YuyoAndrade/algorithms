def removeDuplicates(nums) -> int:
    i = 0
    arr = len(nums)
    while i < arr - 1:
        if nums[i] == nums[i + 1]:
            nums.pop(i + 1)
            arr -= 1
        else:
            i += 1
    return nums


print(removeDuplicates([1, 1, 2, 2, 4, 5, 5, 5, 5]))
