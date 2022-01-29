class Solution:
    def reverseString(self, s: List[str]) -> None:
        """O(n) time | O(1) space"""
        l, r = 0, len(s) - 1
        
        while l < r:
            s[l], s[r] = s[r], s[l]
            l += 1
            r -= 1
        
        return