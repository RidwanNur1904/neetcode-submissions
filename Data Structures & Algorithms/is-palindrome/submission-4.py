class Solution:
    def isPalindrome(self, s: str) -> bool:
        #the first part is a seperator
        s = ''.join(c.lower() for c in s if c.isalnum()) 
        return s == s[::-1]