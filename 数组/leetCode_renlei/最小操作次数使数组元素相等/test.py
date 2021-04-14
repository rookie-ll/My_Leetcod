# 解决不了 [1,100000000]


class Solution:
    def minMoves(self, nums):
        len_nums = len(nums)
        if len_nums == 2:
            return max(nums) - min(nums)
        count_num = 0
        while True:
            idx_num = nums.index(max(nums))
            if sum(nums) == nums[idx_num] * len_nums:
                break
            # elif sum(nums) - nums[idx_num] == min(nums) * (len_nums-1):
            #     return nums[idx_num] - min(nums)
            for i in range(len_nums):
                if i != idx_num:
                    nums[i] += 1
            count_num += 1

        return count_num



if __name__ == '__main__':
    s = Solution()
    # a = [1,1,100000000]
    #   [9,8,7,4,2,1]
    a = [3,2,4,4,8,9]
    print(s.minMoves(a))
