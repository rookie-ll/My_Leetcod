
'''
    1. 当前数小于下一个数：那就是跳过
    2. 当前数大约下一个数
        1. 当前数是第一个数
            1. 直接将当前数赋值为第二个数
        2. 当前数非第一个数
            1. 当前数的下一个数大约当前数的上一个数
                1. 将当前数改变为上一个数--break
            2. 当前数的下一个数小于当前数的上一个数
                1. 将下一个数更改为当前数--break
'''


class Solution:
    def checkPossibility(self, nums):
        change_num = 0

        if len(nums) <= 2: return True

        for i in range(0, len(nums)-2):
            if nums[i] > nums[i+1]:
                if i != 0:
                    if nums[i + 1] >= nums[i - 1]:
                        nums[i+1] = nums[i]
                else:
                    nums[i] = nums[i+1]

                change_num += 1

        if nums[-1] < nums[-2]: change_num += 1

        return True if change_num <= 1 else False



if __name__ == '__main__':
    s = Solution()
    # a = [1,4,2,3]
    # a = [4,2,1]
    # a= [1,3,2]
    # a = [3,4,2,3]
    # a = [5,7,1,8]
    # a = [1,2,3,5,6,7,3,3]
    # a = [8, 1]
    # a = [-1,4,2,3]
    # a = [1,4,1,2]
    a = [1]
    print(s.checkPossibility(a))
