def removeDuplicates(nums) -> int:
    i = 0
    arr = len(nums)

    while i < len(nums) - 2:
        if nums[i] == nums[i + 1] and nums[i] == nums[i + 2]:
            nums.pop(i)
        else:
            i += 1

    return nums


print(removeDuplicates([1, 1, 2, 2, 4, 5, 5, 5, 5]))
