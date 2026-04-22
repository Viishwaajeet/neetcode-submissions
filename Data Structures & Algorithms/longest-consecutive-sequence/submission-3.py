class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        
        l,r, max_seq_len = 0,1, 1

        if len(nums)<2:
            max_sub_len = len(nums)

        while r<len(nums):
            if nums[r] != nums[r-1]+1:
                l = r
            else:
                max_seq_len = max(max_seq_len,r-l+1)
            r += 1

        return max_seq_len