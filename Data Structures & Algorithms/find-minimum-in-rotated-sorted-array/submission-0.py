class Solution:
    def findMin(self, nums: List[int]) -> int:
        mi = sys.maxsize
        for i in range(len(nums)):
            if mi > nums[i]:
                mi = nums[i]
        return mi