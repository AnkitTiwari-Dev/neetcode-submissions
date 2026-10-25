class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new_dict = {}
        for i in range(len(nums)):
            comp = target - nums[i]
            if comp not in new_dict:
                new_dict[nums[i]] = i
            else:
                return[new_dict[comp],i]