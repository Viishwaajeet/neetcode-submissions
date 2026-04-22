class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums = list(set(nums))

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                if nums[i]>nums[j]:
                    nums[i],nums[j] = nums[j],nums[i]
        
        print(nums)

        l,r, max_seq_len = 0,0, 0
        while r<len(nums):
            print(nums[r])
            if nums[r] != nums[r-1]+1:
                # max_seq_len = max(max_seq_len,r-l)
                l = r
            else:
                max_seq_len = max(max_seq_len,r-l+1)
            r += 1

        return max_seq_len