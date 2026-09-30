class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #its a dictionary rememmedber that 
        seen = {}

        for i, a in enumerate(nums):
            diff = target - a
            if diff in seen:
                return [seen[diff], i]
            seen[a] = i 
        