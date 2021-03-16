class Solution(object):
    def findMaxConsecutiveOnes(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 求最大连续的1的个数，数组中只有1和0
        res = 0
        max_nu = 0
        for i in nums:
            # 如果等于1 则累加res
            if i == 1:
                res += 1
            else:
                # 如果不等于1，则为0，,如果max_nu存储的数小于res，那么使用max_nu把连续的数存储起来
                if max_nu < res:
                    max_nu = res
                # 把res初始化为0
                res = 0
        return max_nu


if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes([1, 0, 1, 0, 1, 1, 0,1]))
