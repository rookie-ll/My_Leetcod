
class Solution:
    def maximumProduct1(self, nums) -> int:
        sort_num = sorted(list(nums), key=lambda x: x)
        num1 = sort_num[-1] * sort_num[-2] * sort_num[-3]
        num2 = sort_num[0] * sort_num[1] * sort_num[2]
        num3 = sort_num[0] * sort_num[1] * sort_num[-1]
        return max([num1,num2,num3])
        # return abs(sort_num[-1]) * abs(sort_num[-2]) * abs(sort_num[-3])

    def maximumProduct(self, nums) -> int:
        nums.sort()
        num1 = nums[-1] * nums[-2] * nums[-3]
        num2 = nums[0] * nums[1] * nums[2]
        num3 = nums[0] * nums[1] * nums[-1]
        return max([num1,num2,num3])

# a = [-100,-98,-1,2,3,4]
a = [-100,-2,-3,1]

sol = Solution()

print(sol.maximumProduct(a))


