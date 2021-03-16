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
            if i != 1:
                # 如果不等于1，则为0，,如果max_nu存储的数小于res，那么使用max_nu把连续的数存储起来
                if max_nu < res:
                    max_nu = res
                # 把res初始化为0
                res = 0
        if max_nu < res:
            max_nu = res
        return max_nu

    def findMaxConsecutiveOnes1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        # 求最大连续的1的个数，数组中只有1和0
        # 第二种方法
        max_ls = []
        nu = 0
        for i in nums:
            if i == 1:
                nu += 1
            else:
                max_ls.append(nu)
                nu = 0
        max_ls.append(nu)
        return max(max_ls)



if __name__ == '__main__':
    s = Solution()
    print(s.findMaxConsecutiveOnes1([1, 0, 1, 1]))
