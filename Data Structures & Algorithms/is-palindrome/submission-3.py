class Solution:
    def isPalindrome(self, s: str) -> bool:
        #first make them lower case and then join them together and then check if its alpha numeric
        s = ''.join(c.lower() for c in s if c.isalnum())
        return s == s[::-1]