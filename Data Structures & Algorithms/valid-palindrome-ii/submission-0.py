class Solution:
    def validPalindrome(self, s: str) -> bool:
        l, r = 0, len(s) - 1

        while l < r:
            if s[l] != s[r]:
                #now you would do slicing and shit
                skipL = s[l+1:r+1] # it has to be r+1 so that r is inclusive
                skipR = s[l:r] # ends with R to exclude it 
                return skipL == skipL[::-1] or skipR == skipR[::-1]
            l += 1
            r -= 1
        return True