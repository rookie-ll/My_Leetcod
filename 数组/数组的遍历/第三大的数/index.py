class Solution(object):
    def thirdMax(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        max_nm = max(nums)
        next_nm = 0
        for i in range(len(nums)):
            nums.remove(max_nm)
            if max_nm not in nums: break
        if nums: next_nm = max(nums)
        for i in range(len(nums)):
            nums.remove(next_nm)
            if next_nm not in nums: break
        if nums:
            return max(nums)
        else:
            return max_nm

    def thirdMax1(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        try:
            nums = sorted(list(set(nums)))
            return nums[-3]
        except Exception:
            return nums[0]

if __name__ == '__main__':
    ls = [1, 1, 2]
    s = Solution()
    print(s.thirdMax(ls))

