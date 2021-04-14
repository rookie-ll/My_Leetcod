class Solution:
    def findErrorNums(self, nums):
        if len(nums) == 2 and nums[0] == nums[1]:
            if nums[0] - 1 != 0:
                return [nums[0], nums[0] - 1]
            else:
                return [nums[0], nums[0] + 1]

        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                b_num = nums[i]

        idx = nums.index(b_num)

        if idx != 0:
            if nums[idx - 1] == b_num - 1:
                return [b_num, b_num + 1]
            else:
                return [b_num, b_num - 1]
        elif nums[idx + 2] == b_num + 1:
            return [b_num, b_num - 1]
        else:
            return [b_num, b_num + 1]


