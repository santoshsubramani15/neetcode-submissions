class Solution:
    def isPalindrome(self, s: str) -> bool:
        cleaned = [i.lower() for i in s if i.isalnum()]
        return cleaned == cleaned[::-1]