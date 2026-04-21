class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        seen = dict()
        for c in s:
            if c in seen:
                seen[c] += 1
            else:
                seen[c] = 1
        for c in t:
            if c in seen:
                seen[c] -= 1
            else:
                return False
        for c in seen:
            if seen[c] != 0:
                return False
        return True