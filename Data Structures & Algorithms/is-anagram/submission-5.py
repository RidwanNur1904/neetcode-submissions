class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sset = Counter(s)
        tset = Counter(t)

        if sset == tset: return True    

        return False