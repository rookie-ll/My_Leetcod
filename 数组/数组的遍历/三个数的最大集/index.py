class Solution(object):
    def maximumProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        方法一：排序
        解题思路：
            先排序数组：数组全为负和数组全为正，最大值的情况可能是三个最大的正数和三个最大的负数的乘积
            也有可能是两个最小负数和一个最大正数的乘积
        """
        nums = sorted(nums)
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])

    def maximumProduct1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        """
        方法二：线型扫描
        解题思路：
            先排序数组：数组全为负和数组全为正，最大值的情况可能是三个最大的正数和三个最大的负数的乘积
            也有可能是两个最小负数和一个最大正数的乘积
        """
        # 定义最小数mid1， 和第二小的数 mid2
        mid1 = mid2 = 9007199254740991
        # 定义最大数max1 ，第二大数max2 ，第三大数 max3
        max1 = max2 = max3 = -9007199254740991
        for i in nums:
            # 如果 i 比最小数还小，那么i就是最小数
            if i < mid1:
                # 那么以前的最小数就是第二小数了
                mid2 = mid1
                mid1 = i
            elif i < mid2:
                # 排除比最小数还要小的情况，剩下的就是比第二小数还小的情况
                mid2 = i
            # 如果 i 比最大数还大，那么i就是最大数
            if i > max1:
                max3 = max2
                max2 = max1
                max1 = i
            elif i > max2:
                max3 = max2
                max2 = i
            elif i > max3:
                max3 = i
        # 计算俩种情况，三个最大数相乘  或者 俩个最小数相乘在乘以一个最大数
        return max(mid1 * mid2 * max1, max1 * max2 * max3)


if __name__ == '__main__':
    s = Solution()
    # print(s.maximumProduct([-8, -7, -2, 10, 20]))
    print(s.maximumProduct1([-8, -7, -2, 10, 20]))
