# -*- encoding:utf-8 -*-

class Solution:
    def imageSmoother(self, M):
        # 找出每一个元素周围的数有几个，进行相加后求出平均数生成新列表
        len_m = len(M)

        a_list = []
        a_tupe = []
        for i in range(len_m):
            if i-1 != 0:
                a_list.append(i-1)
            if i +1 < len_m:
                a_list.append(i + 1)
            for j in range(len_m):
                if j - 1 != 0:
                    a_list.append(i - 1)
                if j + 1 < len_m:
                    a_list.append(i + 1)
                a_tupe = [(i,j)for j in a_list for i in a_list]

            count = 0
            num = 0
            for i, j in a_tupe:
                count+=1
                num+=M[i][j]
            a =1


if __name__ == '__main__':
    # s = Solution()
    # a = [[1,1,1],[1,0,1],[1,1,1]]
    # s.imageSmoother(a)
    a = 1
    print(a)