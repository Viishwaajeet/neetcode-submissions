class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        if len(s)<2:
            return len(s)
        res = 1
        seen = set()
        l,r = 0,1
        seen.add(s[l])
        while r<len(s):
            if s[r] not in seen:
                seen.add(s[r])
                res = max(res, r-l+1)
                r += 1
            else:
                seen.remove(s[l])
                l += 1
        return res