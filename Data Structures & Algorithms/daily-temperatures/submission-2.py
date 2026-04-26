class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []
        for i in range(len(temperatures)):
            res.append(0)
            days = 1
            for j in range(i+1, len(temperatures)):
                if temperatures[j]>temperatures[i]:
                    res[i] = days
                    break
                days += 1
        return res