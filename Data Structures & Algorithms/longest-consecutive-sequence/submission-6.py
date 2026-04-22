class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # if len(nums)<2:
        #     return len(nums)

        set_nums = set(nums)

        max_seq_len = 1
        for i in nums:
            if i-1 not in set_nums:
                j = i
                seq_len = 1
                while True:
                    if j+1 in set_nums:
                        seq_len += 1
                        j+=1
                    else:
                        break
                max_seq_len = max(seq_len, max_seq_len)
        
        return max_seq_len