class Solution:
    def findShortestSubArray(self, nums):
        blotter_dict = {}

        # nums中每一个数出现的次数
        for num in nums:
            blotter_dict[num] = blotter_dict.setdefault(num, 0) + 1

        max_num_list = []
        max_d = max(blotter_dict.values())  # 3
        for key, val in blotter_dict.items():
            if val == max_d:
                max_num_list.append([key, val])

        # 找出最短的子集
        subset_len_list = []
        reverse_nums = nums[::-1]
        nums_len = len(nums)  # 7
        for each in max_num_list:  # [[1,3], [2,3]]
            subset_len = nums_len - reverse_nums.index(each[0]) - nums.index(each[0])
            subset_len_list.append(subset_len)

        return min(subset_len_list)



if __name__ == '__main__':
    s = Solution()
    s.findShortestSubArray([1,1,3,2,5,2,3,2,4])
