class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        set_nums = set(nums)
        max_seq_len = 0

        for i in nums:
            if i-1 not in set_nums:
                seq_len = 1
                while i+seq_len in set_nums:
                        seq_len += 1
                max_seq_len = max(seq_len, max_seq_len)
        
        return max_seq_len