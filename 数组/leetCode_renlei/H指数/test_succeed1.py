class Solution:
    def hIndex(self, citations):
        len_num = len(citations)
        number_dict = {i: 0 for i in range(1, len_num+1)}

        for i in citations:
            for each in range(1, len_num+1):
                if i >= each:
                    number_dict[each] += 1
        max_key = 0
        for key, val in number_dict.items():
            if key == val:
                return key
            elif max_key < key and val > key:
                max_key, max_val = key, val

        return max_key


if __name__ == '__main__':
    s = Solution()
    # a = [3,0,6,1,5]
    # a = [1,3,1]
    # a = [0,1,2,3,4,5]
    # a = [0]
    # a = [15,16,1]
    # a = [12,2,3,4,5,6,7,8,9,10,11,15]
    a = [4,4,0,0]
    print(s.hIndex(a))