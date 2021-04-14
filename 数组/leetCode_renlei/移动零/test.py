class Solution:
    def moveZeroes1(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        len_nums = len(nums)

        for i in range(len_nums-1, -1, -1):
            max_idx = i
            for j in range(i,-1,-1):
                if nums[j] == 0:
                    max_idx = j
                    break
                if nums[j] > nums[max_idx]:
                    max_idx = j
            nums[i], nums[max_idx] = nums[max_idx], nums[i]

    def moveZeroes2(self, nums) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """

        len_nums = len(nums)
        not_0 = len_nums-1
        is_0 = len_nums-1
        while not_0 > 0 and is_0 > 0:
            while nums[not_0] == 0 and not_0 > 0:
                not_0 -= 1

            while nums[is_0] != 0 and is_0 > 0:
                is_0 -= 1

            if is_0 < not_0 and nums[is_0] == 0:
                for i in range(is_0, not_0):
                    nums[i], nums[i+1] = nums[i+1], nums[i]
            else:
                is_0 -= 1

        print(nums)

    def moveZeroes_1(self, nums) -> None:

        if not nums:
            return 0
        # 有两个指针，一个指向0，一个遇到不为0的时候进行交换
        j = 0
        for i in range(len(nums)):
            if nums[i]:
                if i == j:
                    j += 1
                else:
                    nums[i], nums[j] = nums[j], nums[i]
                    j += 1

        print(nums)

    def moveZeroes(self, nums) -> None:

        j = 0
        for i in range(len(nums)):
            if nums[i]:
                nums[j] = nums[i]
                j += 1

        for i in range(j, len(nums)):
            nums[i] = 0

        print(nums)



if __name__ == '__main__':
    s = Solution()
    a = [0,1,0,3,12,6,2,6,1,5,0,7,0,2,9,0,1,4,0]
    # a = [0,0,1]
    # a = [0,0]
    # a = [2,1]
    # a = [1,3,4,5,0,7,0,3,6,7,0,2]
    s.moveZeroes(a)
