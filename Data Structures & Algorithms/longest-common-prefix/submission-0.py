class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        max_len = 0
        for i in strs:
            max_len = max(max_len, len(i))
        
        l_prefix = ''
        for i in range(max_len):
            ch = strs[0][i]
            for j in strs:
                if j[i] != ch:
                    return l_prefix
            else:
                l_prefix += ch