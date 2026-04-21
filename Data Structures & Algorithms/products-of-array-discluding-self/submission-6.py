class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        n = len(nums)
        leftProd = [1]*n
        for i in range(n-1):
            leftProd[i+1] = leftProd[i]*nums[i]
        rightProd = [1]*n
        for i in range(n-1,0,-1):
            rightProd[i-1] = rightProd[i]*nums[i]
        res = []
        for i in range(n):
            res.append(leftProd[i]*rightProd[i])
        return res