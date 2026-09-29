class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        i = 0;
        for num in nums:
            offset = target - num
            if offset in seen:
                return [seen[offset],i]
            seen[num] = i
            i += 1
        return[0,0]