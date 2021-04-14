# -*- coding:utf8 -*-

'''
    # 495
    解题思路：
        此题的核心：
            重点1：要清楚两次攻击的持续时间是否有重叠，如果有重叠，找出第一次攻击作数的时间，
            重点2：最后一次攻击他一定是整个持续时间
        1. 整个攻击时间是持续递增的
        2. 两次相继的攻击会出现两种情况
            * 两次攻击中出现了重叠的时间，重叠中的时间只算作一次攻击
                --计算规则：如果前一次的攻击时间加上持续时间 大于了 后一次的攻击时间，那么出现了重叠时间
                -* 核心： 如果出现了重叠时间，那么第一次的攻击只有在发动第二次攻击之前的时间才作数，第二
                        次攻击开始后的持续时间都算入第二次攻击持续时间，想要求得第一次攻击作数的持续时间，
                        就是用第二次的持续时间减掉第一次开始时间，那么区间就是第一次攻击作数的时间将其加入
                        到总计时中，以此循环
            * 两次攻击中没有出现重叠的时间，那么两次攻击互不影响持续时间
                ** 直接将上一次的持续时间加入总计时中
'''


class Solution:
    def findPoisonedDuration(self, timeSeries, duration: int) -> int:

        # 每个时间点都会进行攻击，并持续duration的时间

        # 将每一次的攻击时间都放入到列表中
        num_time = 0 # res

        if not timeSeries: return 0  # 判空

        number_per = timeSeries[0]

        for number in timeSeries[1:]:
            if number - number_per >= duration:
                num_time += duration
            else:
                num_time += number - number_per
            number_per = number

        num_time += duration

        return num_time


if __name__ == '__main__':
    timeseries = [1,2,3,4,5]

    duration = 5

    s = Solution()

    print(s.findPoisonedDuration(timeseries, duration))

