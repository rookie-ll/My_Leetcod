class Solution:
    def findDuplicates(self, nums):

        len_nums = len(nums)
        ret = []
        for num in nums:
            nums[(num - 1) % len_nums] += len_nums

            if nums[(num - 1) % len_nums] > len_nums * 2:

                ret.append((num - 1) % len_nums + 1)

        return ret

if __name__ == '__main__':
    s = Solution()
    a = [10,2,5,10,9,1,1,4,3,7]
    a = [4,3,2,7,8,2,3,1]
    a = [2,2]
    print(s.findDuplicates(a))