class Solution:
    def findDuplicates(self, nums):

        len_nums = len(nums)
        for num in nums:
            nums[(num - 1) % len_nums] = nums[(num - 1) % len_nums] + len_nums

        for i, num in enumerate(nums):
            if num > len_nums * 2:
                nums[i] = i + 1
            else:
                nums[i] = num * -1
        a = []
        for num in nums:
            if num > 0:
                a.append(num)

        return a

if __name__ == '__main__':
    s = Solution()
    a = [10,2,5,10,9,1,1,4,3,7]
    a = [4,3,2,7,8,2,3,1]
    a= [2,2]
    print(s.findDuplicates(a))