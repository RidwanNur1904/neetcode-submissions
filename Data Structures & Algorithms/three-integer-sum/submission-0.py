class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        #remember I am returning a list
        result = []
        nums.sort()
        #remember three sum is basically two sum + pointers
        for i, a in enumerate(nums):
            #this is to check that its not hte same value 
            if i > 0 and a == nums[i-1]:
                continue
            #left should be the start of the list and right should end of the list
            l,r = i+1, len(nums) - 1
            #both pointers cannot be the same
            while l < r:
                threesum = a + nums[l] + nums[r]

                if threesum > 0:
                    r -= 1
                elif threesum < 0:
                    l += 1
                else:
                    result.append([a, nums[l], nums[r]])
                    l += 1
                    r -= 1
                    while nums[l] == nums[l-1] and l < r:
                        l += 1
        return result
            
