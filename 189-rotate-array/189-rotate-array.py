class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """O(n) time | O(1) space"""
        n = len(nums) 
        k = k % len(nums)
        j = 0
        
        while n > 0 and k % n != 0:
            for i in range(0, k):
                # swap
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i]
            
            n = n - k
            j = j + k
            k = k % n
        