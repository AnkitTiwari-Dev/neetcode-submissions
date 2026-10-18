class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        pref = [1]
        l = len(nums)
        product = 1
        for i in range(l - 1):
            product *= nums[i]
            pref.append(product)
        suff = [1]
        product = 1
        for i in reversed(nums[1:]):
            product *= i
            suff.append(product)
        res = []
        for i in range(l):
            n = (pref[i] * suff[l - i - 1])
            res.append(n)
        return res