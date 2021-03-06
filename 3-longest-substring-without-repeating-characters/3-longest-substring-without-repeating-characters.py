class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """O(n) time | O(1) space"""
        start = maxLength = 0
        usedChar = {}
        
        for idx, char in enumerate(s):
            if char in usedChar:
                start = max(start, usedChar[char] + 1)
                
            maxLength = max(maxLength, idx - start + 1)
            usedChar[char] = idx
        
        return maxLength