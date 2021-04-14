class Solution:
    def hIndex(self, citations):
        len_num = len(citations)
        blotter_list = []
        for i in citations:
            if i < len_num:
                blotter_list.append(i)

        blotter_number = 0
        number_list = []
        for num in range(1, len_num +1):
            for i in citations:
                if i >= num:
                    blotter_number += 1
            if blotter_number >= num:
                number_list.append(num)
                blotter_number = 0
            else:
                blotter_number = 0

        if number_list:
            return max(number_list)
        return 0

        # if blotter_list:
        #     max_blotter = max(blotter_list)
        #     if max_blotter == 0:
        #         return 0
        # else:
        #     return len_num

        return max_blotter



if __name__ == '__main__':
    s = Solution()
    # a = [3,0,6,1,5]
    # a = [1,3,1]
    # a = [0,1,2,3,4,5]
    # a = [0]
    # a = [15,16]
    a = [12,2,3,4,5,6,7,8,9,10,11,15]
    # a = [4,4,0,0]
    print(s.hIndex(a))