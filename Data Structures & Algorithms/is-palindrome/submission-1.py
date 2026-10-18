import string
class Solution:
    def isPalindrome(self, s: str) -> bool:
        st = s.strip()
        a = ""
        for c in s:
            if not c.isalnum():
                continue
            a += c.lower()
        return a == a[::-1]