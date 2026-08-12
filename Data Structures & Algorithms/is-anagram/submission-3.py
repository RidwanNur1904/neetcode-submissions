class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_set = Counter(s)
        t_set = Counter(t)

        if s_set == t_set: return True
        else: return False
