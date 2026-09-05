class Solution:
    def trap(self, height: List[int]) -> int:
        lo,high = 0,len(height)-1
        left_max,right_max,water = 0,0,0
        while lo <high:
            if height[lo] < height[high]:
                left_max = max(left_max,height[lo])
                water += left_max - height[lo]
                lo += 1
            else:
                right_max =max(right_max,height[high])
                water += right_max - height[high]
                high -=1
        return water
        
        