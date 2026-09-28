class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        #count is basically like how many times does that specific one occur and shit

        if nums.count(0) > 1: return [0] * len(nums)

        #the product of something without it
        product = math.prod(nums)

        productWO0 = 1
        for n in nums:
            if n == 0: continue
            productWO0 *= n

        res = []
        for n in nums:
            if n == 0:
                res.append(productWO0)
            else:
                res.append(int(product/n))

        return res