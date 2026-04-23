class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        l,r = 0, len(height)-1
        max_lh, max_rh = height[l], height[r]
        while l<r:
            if height[l]<=height[r]:
                l+=1
                if height[l]>max_lh:
                    max_lh = max(max_lh, height[l])
                else:
                    volume += min(max_lh,max_rh)-height[l]
            else:
                r-=1
                if height[r]>max_rh:
                    max_rh = max(max_rh, height[r])
                else:
                    volume += min(max_lh,max_rh)-height[r]
        return volume