class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Ensure nums1 is the smaller array to optimize binary search complexity
        A, B = nums1, nums2
        if len(A) > len(B):
            A, B = B, A
        
        m, n = len(A), len(B)
        low, high = 0, m
        half_len = (m + n + 1) // 2
        
        while low <= high:
            i = (low + high) // 2
            j = half_len - i
            
            # Retrieve elements around the partition boundary, using infinity for out-of-bound indices
            A_left_max = A[i - 1] if i > 0 else float('-inf')
            A_right_min = A[i] if i < m else float('inf')
            B_left_max = B[j - 1] if j > 0 else float('-inf')
            B_right_min = B[j] if j < n else float('inf')
            
            # Check if we have partitioned the arrays correctly
            if A_left_max <= B_right_min and B_left_max <= A_right_min:
                # Odd combined length: return the maximum of the left partition
                if (m + n) % 2 == 1:
                    return float(max(A_left_max, B_left_max))
                # Even combined length: return the average of the middle elements
                else:
                    return (max(A_left_max, B_left_max) + min(A_right_min, B_right_min)) / 2.0
            elif A_left_max > B_right_min:
                high = i - 1  # Too many elements from A in the left partition, move left
            else:
                low = i + 1   # Too few elements from A in the left partition, move right
                
        return 0.0