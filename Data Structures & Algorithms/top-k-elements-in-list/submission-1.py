class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        counts = {}
        freq = [[] for i in range(len(nums)+1)]
        for i in nums:
            counts[i] = 1 + counts.get(i, 0)
        for num,cnt in counts.items():
            freq[cnt].append(num)
        
        res = []
        for i in range(len(freq)-1,0,-1):
            for n in freq[i]:
                res.append(n)
                if len(res)==k:
                    return res