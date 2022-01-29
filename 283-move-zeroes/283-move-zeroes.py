class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """O(n) time | O(1) space"""
        l = 0
        
        for idx in range(len(nums)):
            if nums[idx] != 0 and nums[l] == 0:
                nums[idx], nums[l] = nums[l], nums[idx]
                
            if nums[l] != 0:
                l += 1
                
        return