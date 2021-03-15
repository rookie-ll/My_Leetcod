"""
给定一个数组 nums，编写一个函数将所有 0 移动到数组的末尾，同时保持非零元素的相对顺序。
示例:
    输入: [0,1,0,3,12]
    输出: [1,3,12,0,0]
说明:
    必须在原数组上操作，不能拷贝额外的数组。
    尽量减少操作次数。
"""


class Solution(object):
    def moveZeroes(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 采用左右指针
        left_per = right_per = 0
        for i in range(len(nums)):
            if nums[right_per] != 0:
                nums[left_per], nums[right_per] = nums[right_per], nums[left_per]
                left_per += 1
            right_per += 1

    def moveZeroes2(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # 先把前面的零都换成非零的数，然后再把后面换过去的数替换回来零，i为控制有多少非零数的位置参数，i下标的右面都是零
        n = len(nums)
        i = -1
        j = 0
        # nums[0....i]表示非0元素的数列,初始值i=-1
        while j <= n - 1:
            if nums[j] != 0:
                i += 1
                nums[i] = nums[j]
            j += 1
        for k in range(i + 1, n):
            nums[k] = 0


if __name__ == '__main__':
    s = Solution()
    ls = [0, 1, 0, 3, 12]
    # s.moveZeroes(ls)
    # s.moveZeroes2(ls)
    for i in range(3,4):
        print(i)