class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        hash_table = {}
        for i in range(len(nums)):
            hash_table[nums[i]] = (i,target-nums[i])
        
        for i in nums:
            if hash_table[i][1] in hash_table:
                return [hash_table[i][0], hash_table[hash_table[i][1]][0]]