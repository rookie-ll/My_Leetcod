class Solution:
    def findShortestSubArray(self, nums):
        # [第一次出现的位置，最后一次出现的位置，出现的次数]
        blotter_dict = {}

        for idx, num in enumerate(nums):
            blotter_dict[num] = [
                                blotter_dict.setdefault(num, [idx, idx, 0])[0],
                                idx,
                                blotter_dict.setdefault(num, [idx, idx, 0])[2] +1
                ]

        b_count = min_len = 0
        for per_i, next_i, count in blotter_dict.values():
            if b_count < count:
                b_count = count
                min_len = next_i - per_i + 1
            elif b_count == count:
                b_len = next_i - per_i + 1
                if b_len < min_len:
                    min_len = b_len

        return min_len


if __name__ == '__main__':
    s = Solution()
    s.findShortestSubArray([1,1,1,3,2,5,2,2,4])