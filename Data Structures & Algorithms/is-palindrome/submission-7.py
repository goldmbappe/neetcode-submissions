class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean =""
        for i in s:
            if i.isalnum():
                clean += i.lower()
        chars = list(clean)
        reverse = chars[::-1]
        return chars == reverse