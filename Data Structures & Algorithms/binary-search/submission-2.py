class Solution:
    def search(self, nums: List[int], target: int) -> int:
        left, right = 0, len(nums)-1
        res = self.binary_search(nums, target, left, right)
        return res
        
    def binary_search(self, nums, target, left, right):
        mid = left + (right-left)//2
        if nums[mid]==target:
            return mid
        elif left>=right:
            return -1
        elif nums[mid]<target:
            left = mid + 1
        else:
            right = mid -1
        return self.binary_search(nums, target, left, right)