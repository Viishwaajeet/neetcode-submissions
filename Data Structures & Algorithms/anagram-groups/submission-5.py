class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for i in strs:
            tup = [0 for i in range(26)]
            for j in i:
                tup[ord(j)%97] += 1
            if tuple(tup) not in res:
                res[tuple(tup)] = [i]
            else:
                res[tuple(tup)].append(i)
        return [x for x in res.values()]