'''
    每次都有一个数不加，那么想要相等就需要每次让最小的数追平最大的数，
    每次在追最大的这个数的时候，其他的数都会一起加1，所以最小的这个数和其他的数差值不变，
    当追平了最大的这个数再追下一个大过他的数，下一个大过他的数和开始的差值不变，所以最小多少次可以
    全部相同在于最小的数和每一个数的差值相加最后的和，就是最小的次数使数组中的所有的数全部都相同
'''


class Solution:
    def minMoves(self, nums):
        min_number = min(nums)
        sum_num = 0
        for num in nums:
            sum_num+= num - min_number

        return sum_num



if __name__ == '__main__':
    s = Solution()
    a = [1,1,100000000]
    #   [9,8,7,4,2,1]
    # a = [3,2,4,4,8,9]
    a= [1,2,3]
    print(s.minMoves(a))
