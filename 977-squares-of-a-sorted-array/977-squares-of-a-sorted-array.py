class Solution:
    """O(n) time | O(n) space"""
    def sortedSquares(self, nums: List[int]) -> List[int]:
        left = 0
        right = len(nums) - 1
        output = []
        
        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                output.append(nums[left]**2)
                left += 1
            else:
                output.append(nums[right]**2)
                right -= 1
                
        return output[::-1]