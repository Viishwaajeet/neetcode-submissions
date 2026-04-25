class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tup = tuple([0 for i in range(26)])