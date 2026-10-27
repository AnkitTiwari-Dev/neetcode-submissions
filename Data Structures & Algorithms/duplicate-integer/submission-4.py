class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        new_dict = {}
        for i in range(len(nums)):
            if nums[i] in new_dict:
                return True
            new_dict[nums[i]] = i
        return False