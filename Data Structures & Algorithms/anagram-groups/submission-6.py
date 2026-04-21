class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        grouped = {}

        for i in strs:
            freq = [0] * 26
            for j in i:
                freq[ord(j)-97] += 1
            if tuple(freq) not in grouped:
                grouped[tuple(freq)] = [i]
            else:
                grouped[tuple(freq)].append(i)
        
        return list(grouped.values())