class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        min_len = len(strs[0])
        for i in strs:
            min_len = min(min_len, len(i))

        l_prefix = ''
        for i in range(min_len):
            ch = strs[0][i]
            for j in strs:
                if j[i] != ch:
                    return l_prefix
            else:
                l_prefix += ch
        else:
            return l_prefix