# -*- encoding:utf-8 -*-

class Solution:
    def imageSmoother(self, M):
        # 找出每一个元素周围的数有几个，进行相加后求出平均数生成新列表
        len_h = len(M)
        if M:
            len_w = len(M[0])
        else:
            return []

        M_list = [['' for i in range(len_w)] for j in range(len_h)]
        for i in range(len_h):
            a_list = []
            if i == 0:
                if len_h -1 != 0:
                    a_list.extend([i, i + 1])
                else:
                    a_list.append(i)
            elif i == len_h - 1:
                if len_h -1 != 0:
                    a_list.extend([i, i - 1])
                else:
                    a_list.append(i)
            else:
                a_list.extend([i, i - 1, i + 1])
            for j in range(len_w):
                a_tupe = []
                b_list = []
                if j == 0:
                    if len_w - 1 != 0:
                        b_list.extend([j, j + 1])
                    else:
                        b_list.append(j)
                elif j == len_w - 1:
                    if len_w - 1 != 0:
                        b_list.extend([j, j - 1])
                    else:
                        b_list.append(j)
                else:
                    b_list.extend([j, j - 1, j + 1])

                a_tupe = [(i,j)for j in b_list for i in a_list]

                count = 0
                num = 0
                for ai, aj in a_tupe:
                    count+=1
                    num+=M[ai][aj]

                M_list[i][j] = num // count
        return M_list


if __name__ == '__main__':
    s = Solution()
    a = [[1,1,1,1],
         [1,0,1,1],
         [1,1,1,1],
         [1,1,1,1]]
    a = [
        [2,3,4],
        [5,6,7],
        [8,9,10],
        [11,12,13],
        [14,15,16]]
    a = [[1]]
    print(s.imageSmoother(a))
