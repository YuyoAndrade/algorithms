def singleNumber(nums):
    while True:
        print(nums)
        if len(nums) == 1 or nums[0] not in nums[1:]:
            return nums[0]
        breakpoint()
        nums.remove(nums[0])


singleNumber([2, 2, 1])