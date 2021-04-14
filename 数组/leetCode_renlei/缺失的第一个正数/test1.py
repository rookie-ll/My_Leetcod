class Solution:
    def firstMissingPositive(self, nums) -> int:
        len_nums = len(nums)

        # 将所有负数，不相干的踢出去，踢使用大过最大长度
        # for i, num in enumerate(nums):
        #     if num <= 0:
        #         nums[i] = len_nums + 3

        # 将每一个小于最大长度的数所对应的下标的数进行修改变为负数，这样当遍历到他后，就不会修改掉他本该修改的位置
        for i, num in enumerate(nums):
            if num <= len_nums and num > 0:
                nums[(num - 1) % len_nums] = nums[(num -1) % len_nums] + len_nums

        # 找出第一个为正的数
        for i, num in enumerate(nums):
            if num != i+1:
                return i + 1

        return len_nums + 1


if __name__ == '__main__':
    s = Solution()
    a = [7,8,9,11,12]
    a = [3,4,-1,1]
    # a = [1,2,0]
    # a = [1,2,4]
    # a = [1,1]
    print(s.firstMissingPositive(a))