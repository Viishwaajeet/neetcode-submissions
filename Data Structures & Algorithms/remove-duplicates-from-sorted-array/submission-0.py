class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        seen = set()
        count = 0
        for i in range(len(nums)):
            if nums[i] not in seen:
                seen.add(nums[i])
                nums[count], nums[i] = nums[i], nums[count]
                count += 1
        return count