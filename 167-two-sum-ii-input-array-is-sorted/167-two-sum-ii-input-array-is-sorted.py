class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """O(n) time | O(1) space"""
        l = 0 
        r = len(numbers) - 1
        
        while l < r:
            if numbers[l] + numbers[r] == target:
                return [l + 1, r + 1]
            
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1