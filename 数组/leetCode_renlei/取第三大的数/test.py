class Solution:
    def thirdMax(self, nums) -> int:
        try:
            return sorted(list(set(nums)))[-3]
        except Exception:
            return sorted(list(set(nums)))[-1]