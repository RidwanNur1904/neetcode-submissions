class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            res += str(len(s)) + "#" + s
        return res

    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            # Find the delimiter '#'
            while s[j] != '#':
                j += 1
            
            # Read the word length
            length = int(s[i:j])
            
            # Extract the word using the length
            res.append(s[j + 1 : j + 1 + length])
            
            # Move pointer i to the start of the next encoded string
            i = j + 1 + length
            
        return res

