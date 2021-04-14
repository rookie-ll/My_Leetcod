class Solution:
    def checkPossibility(self, nums):

        len_nums = len(nums) - 1

        change_num = 0

        for i in range(len_nums-1, -1, -1):
            if nums[i] <= nums[i+1]:
                continue
            else:
                # nums[i + 1] = nums[i] + 1
                change_num += 1

        return True if change_num <= 1 else False


if __name__ == '__main__':
    s = Solution()
    # a = [4,2,3]
    # a = [4,2,1]
    # a= [1,3,2]
    a = [3,4,2,3]
    # a = [1,2,3,5,6,3,3]
    print(s.checkPossibility(a))
