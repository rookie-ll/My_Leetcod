class Solution(object):
    def findPoisonedDuration(self, timeSeries, duration):
        """
        :type timeSeries: List[int]
        :type duration: int
        :rtype: int
        """
        res = 0
        # 判断数组是否为空，为空则直接 return 0
        if not timeSeries: return 0
        # 判断数组是否只有一次攻击，只有一次攻击则直接返回持续时间
        if len(timeSeries) == 1: return duration
        for i in range(len(timeSeries) - 1):
            if timeSeries[i + 1] - timeSeries[i] >= duration:
                res += duration
            else:
                # 通过累加俩秒攻击间隔的方式累加重复的的中毒时间
                res = res + (timeSeries[i + 1] - timeSeries[i])
        res += duration
        return res

    '''
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
    def findPoisonedDuration1(self, timeSeries, duration: int) -> int:

        # 每个时间点都会进行攻击，并持续duration的时间

        # 将每一次的攻击时间都放入到列表中
        if not timeSeries: return 0

        if len(timeSeries) == 1: return duration

        res = 0
        start = timeSeries[0]
        end = start + duration
        for i in range(1, len(timeSeries)):
            if timeSeries[i] <= end:
                end = timeSeries[i] + duration
            else:
                res += end - start
                start = timeSeries[i]
                end = start + duration
        res += end - start
        return res



if __name__ == '__main__':
    # [1, 2], 2  ==> 3
    # [1, 4], 2  ==> 4
    s = Solution()
    res = s.findPoisonedDuration1([1, 2, 3, 4, 5, 6, 7, 8, 9], 5)
    print(res)
