class Solution:
    def search(self, nums: List[int], target: int) -> int:
        """O(log(n)) time | O(1) space"""
        low = 0
        high = len(nums) - 1
        
        while low <= high:
            mid = (low + high) // 2
            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                high = mid - 1
                
            if nums[mid] < target:
                low = mid + 1
                
        return -1