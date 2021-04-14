class Solution:
    def generate(self, numRows: int):

        # 生成这样一个列表
        rows_list = [[1 for _ in range(1, i+1)] for i in range(1, numRows + 1)]
        # 生成列表中的值
        for i in range(numRows):
            if i <= 1:
                # bollter_list.append(
                #     [1 for j in range(i)]
                # )
                continue
            else:
                for j in range(len(rows_list[i-1])-1):
                   rows_list[i][j+1] = rows_list[i-1][j] + rows_list[i-1][j+1]

        return rows_list



if __name__ == '__main__':
    s = Solution()
    a = 2
    print(s.generate(a))

