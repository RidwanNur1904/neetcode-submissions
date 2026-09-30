class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        #for sliding windows make right and left be 0 at the start
        l = 0
        sett = set()
        max_len = 0

        for r in range(len(s)):
            #while the slider for right is in the thing
            while s[r] in sett:
                sett.remove(s[l])
                l += 1

            sett.add(s[r])
            max_len = max(max_len, r-l+1)

        return max_len
            
