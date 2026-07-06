class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        # Base Case: If there's only one element, it must be our answer!
        if len(nums) <= 1:
            return nums[0]
            
        pivot = nums[len(nums) // 2]
        
        # Keep your exact list comprehensions (using 'x' instead of 'k')
        left  = [x for x in nums if x < pivot] 
        mid   = [x for x in nums if x == pivot]  
        right = [x for x in nums if x > pivot] 
        
        # Count how many elements are in the right and middle sections
        len_r = len(right)
        len_m = len(mid)
        
        if k <= len_r:
            # Case 1: The k-th largest is somewhere in the 'right' (larger) side
            return self.findKthLargest(right, k)
            
        elif k <= len_r + len_m:
            # Case 2: The k-th largest falls right into the 'mid' section (the pivot)
            return mid[0]
            
        else:
            # Case 3: The k-th largest is in the 'left' (smaller) side.
            # We subtract len_r and len_m because we are completely skipping those larger numbers!
            return self.findKthLargest(left, k - len_r - len_m)