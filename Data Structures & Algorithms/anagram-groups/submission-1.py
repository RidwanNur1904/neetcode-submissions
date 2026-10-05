class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #basically acts as a fingerprint
        anagrams_dict = defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                #ord is used to represent the unicode
                count[ord(c) - ord('a')] += 1

            key = tuple(count)
            anagrams_dict[key].append(s)

        return list(anagrams_dict.values())