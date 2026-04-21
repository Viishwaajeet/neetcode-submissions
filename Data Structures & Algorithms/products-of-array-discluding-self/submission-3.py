class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        product = 1
        for i in nums:
            if i!=0:
                product *= i

        res = []
        if 0 in nums:
            for i in nums:
                if i==0 and nums.count(0)==1:
                    res.append(product)
                else:
                    res.append(0)
        else:
            res = [int(product/i) for i in nums]
        
        return res