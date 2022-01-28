class Solution:
    """O(n) time | O(n) space"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        l, r = 0, len(nums) - 1
        output = [0] * len(nums)
        
        while l <= r:
            left, right = abs(nums[l]), abs(nums[r])
            
            if left > right:
                output[r - l] = left * left
                l += 1
            else:
                output[r - l] = right * right
                r -= 1
                
        return output