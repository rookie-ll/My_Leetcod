class Solution:
    def findDisappearedNumbers(self, nums):

        for num in nums:
            nums[abs(num) - 1] = abs(nums[abs(num) - 1]) * -1

        return [i+1 for i, a in enumerate(nums) if a > -1]


if __name__ == '__main__':
    s = Solution()
    a= [4,3,2,7,8,2,3,1]
    print(s.findDisappearedNumbers(a))