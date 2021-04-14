class Solution:
    def hIndex(self, citations):
        len_num = len(citations)

        blotter_number = 0
        number_list = []
        for num in range(1, len_num + 1):
            for i in citations:
                if i >= num:
                    blotter_number += 1
            if blotter_number >= num:
                number_list.append(num)
                blotter_number = 0
            else:
                blotter_number = 0


        return max(number_list) if number_list else 0


if __name__ == '__main__':
    s = Solution()
    # a = [3,0,6,1,5]
    a = [1,3,100]
    # a = [0,1,2,3,4,5]
    # a = [0]
    # a = [15,16,1]
    # a = [12,2,3,4,5,6,7,8,9,10,11,15]
    # a = [4,4,0,0]
    print(s.hIndex(a))