class Solution:
    def hIndex(self, citations) -> int:
        blotter_list = []
        blotter_number = 0
        for num in citations:
            for i in citations:
                if i >= num:
                    blotter_number += 1
            if blotter_number >= num:
                blotter_list.append(num)
                blotter_number = 0
            else:
                blotter_number = 0
        if blotter_list:
            return max(blotter_list)
        else:
            return 0 if min(citations) <= 0 else 1


if __name__ == '__main__':
    s = Solution()
    a = [3,0,6,1,5]
    # a = [1,3,1]
    # a = [0,1,2,3,4,5]
    print(s.hIndex(a))