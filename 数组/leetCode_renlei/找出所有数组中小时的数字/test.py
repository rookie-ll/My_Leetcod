class Solution:
    def findDisappearedNumbers(self, nums):

        blotter_list = []

        for i in range(1, len(nums) + 1):
            if i not in set(nums):
                blotter_list.append(i)

        return blotter_list
