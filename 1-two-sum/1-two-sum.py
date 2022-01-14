class Solution:
    """O(n) time | O(n) space"""
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        pairs = {}
        
        for idx in range(len(nums)):
            delta = target - nums[idx]
            
            if delta in pairs:
                return [pairs[delta], idx]
            
            pairs[nums[idx]] = idx