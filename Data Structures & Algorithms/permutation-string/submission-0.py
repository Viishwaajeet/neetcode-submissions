class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count = {}
        for i in s1:
            count[i] = 1 + count.get(i,0)  
        for i in s2:
            if i in count:
                count[i] -= 1
        return all(x==0 for x in count.values())