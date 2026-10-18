class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        new_set = set(nums)
        max_count = 0
        for s in new_set:
            if s-1 in new_set:
                continue
            count = 1
            while s+1 in new_set:
                count += 1
                s+=1
            if count > max_count:
                max_count = count
        return max_count