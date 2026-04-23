class Solution:
    def trap(self, height: List[int]) -> int:
        volume = 0
        l,r = 0, len(height)-1
        max_lh, max_rh = height[l], height[r]
        while l<r:
            if height[l]<=height[r]:
                if height[l+1]>max_lh:
                    l+=1
                    max_lh = max(max_lh, height[l])
                else:
                    volume += min(max_lh,max_rh)-height[l+1]
                    l+=1
            else:
                if height[r-1]>max_rh:
                    r-=1
                    max_rh = max(max_rh, height[r])
                else:
                    volume += min(max_lh,max_rh)-height[r-1]
                    r-=1
        return volume