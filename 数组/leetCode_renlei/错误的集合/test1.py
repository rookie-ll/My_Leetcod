class Solution:
    def findErrorNums(self, nums):
        nums.sort()

        for i in range(1, len(nums)):
            if nums[i] == nums[i - 1]:
                b_num = nums[i]

        for i in range(1, nums[-1]):
            if i not in nums:
                return [b_num, i]

        return [b_num, nums[-1] + 1]

s = Solution()
a = [1, 3, 3]
a = [3,2,3,4,6,5]
a= [2,2]
a = [1,1,3]
a = [2,2,3]
a = [1,1]
# a = [2,2]
print(s.findErrorNums(a))


