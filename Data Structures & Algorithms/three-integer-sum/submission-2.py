class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        res = []
        nums.sort()
        l = len(nums)
        triplets = set()
        for i in range(l-2):
            new_dict = {}
            for j in range(i+1,l):
                add = nums[i] + nums[j]
                if -add in new_dict:
                    triplets.add((nums[i],nums[j],-add))
                new_dict[nums[j]] = j
        for tup in triplets:
            res.append(list(tup))
        return res

        