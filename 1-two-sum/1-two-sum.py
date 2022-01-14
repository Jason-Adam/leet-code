class Solution:
    """O(n) time | O(n) space"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        
        for idx, num in enumerate(nums):
            delta = target - num
            
            if delta in pairs:
                return [pairs[delta], idx]
            
            pairs[num] = idx