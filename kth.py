import numpy as np

class Solution:
    def smallestDistancePair(self, nums: List[int], k: int) -> int:
        # 1. Convert to a sorted NumPy array for fast indexing
        nums = np.sort(np.array(nums))
        n = len(nums)
        
        # 2. Define the Search Space
        low, high = 0, int(nums[-1] - nums[0])
        
        while low < high:
            mid = (low + high) // 2
            
            # 3. Vectorized "Pair Counting"
            # For each number at index i, find how many numbers 
            # are within the range [nums[i], nums[i] + mid]
            # searchsorted is optimized C-code under the hood
            upper_bounds = np.searchsorted(nums, nums + mid, side='right')
            
            # The count of pairs for each i is (upper_bound - current_index - 1)
            count = np.sum(upper_bounds - np.arange(n) - 1)
            
            if count >= k:
                high = mid
            else:
                low = mid + 1
                
        return int(low)        