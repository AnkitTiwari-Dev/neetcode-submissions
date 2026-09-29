class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        num_list = {}
        for i in nums:
            if i in num_list.keys():
                return True
            num_list[i] = 1
        return False
        