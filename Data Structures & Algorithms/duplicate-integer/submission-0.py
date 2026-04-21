class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        checked_list = set()
        for i in nums:
            if i in checked_list:
                return True
            checked_list.add(i)
        return False