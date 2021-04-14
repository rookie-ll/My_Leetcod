class Solution:
    def checkPossibility(self, nums):
        change_num = 0
        import copy
        numsa = copy.deepcopy(nums)
        if len(nums) == 1:
            return True

        while True:
            jubge = True
            for i in range(0, len(nums)-2):
                if nums[i] > nums[i+1]:
                    nums[i] = nums[i+1] = max(nums[i], nums[i+1])
                    change_num += 1
                    jubge = False

            if nums[-1] < nums[-2]:
                nums[-1] = nums[-2]
                change_num += 1
                jubge = False

            if change_num > 1 or jubge:
                break

        a =  True if change_num <= 1 else False
        change_num = 0
        while True:
            jubge = True
            for i in range(0, len(numsa)-2):
                if numsa[i] > numsa[i+1]:
                    numsa[i] = numsa[i+1] = min(numsa[i], numsa[i+1])
                    change_num += 1
                    jubge = False

            if numsa[-1] < numsa[-2]:
                numsa[-1] = numsa[-2]
                change_num += 1
                jubge = False

            if change_num > 1 or jubge:
                break

        b = True if change_num <= 1 else False

        return a or b



if __name__ == '__main__':
    s = Solution()
    a = [4,2,3]
    # a = [4,2,1]
    # a= [1,3,2]
    a = [3,4,2,3]
    a = [5,7,1,8]
    a = [1,2,3,5,6,7,3]
    a = [8, 1]
    print(s.checkPossibility(a))
