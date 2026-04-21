class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq = {}

        for i in nums:
            freq[i] = freq.get(i, 0) + 1

        m = 0
        for i in freq.items():
            m = max(m, i[1])

        for i in freq.items():
            if i[1]==m:
                return i[0]