class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hashs = {}
        hasht = {}
        for i in s:
            if i in hashs:
                hashs[i] += 1
            else:
                hashs[i] = 1
        for i in t:
            if i in hasht:
                hasht[i] += 1
            else:
                hasht[i] = 1
        return hashs==hasht