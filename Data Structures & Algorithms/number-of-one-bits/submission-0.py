class Solution:
    def hammingWeight(self, n: int) -> int:
        binary = bin(n)
        ones = binary.count("1")

        return ones