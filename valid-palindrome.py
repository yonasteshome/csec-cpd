class Solution:
    def isPalindrome(self, s: str) -> bool:
        y=""
        for i in s:
            if i.isalnum():
                y+=i.lower()
        return y == y[::-1]