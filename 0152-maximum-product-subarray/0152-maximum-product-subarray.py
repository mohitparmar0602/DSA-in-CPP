from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        if not nums:
            return 0
        
        max_so_far = nums[0]
        current_max = nums[0]
        current_min = nums[0]
        
        for num in nums[1:]:
            temp = max(num, current_max * num, current_min * num)
            current_min = min(num, current_max * num, current_min * num)
            current_max = temp
            max_so_far = max(max_so_far, current_max)
            
        return max_so_far