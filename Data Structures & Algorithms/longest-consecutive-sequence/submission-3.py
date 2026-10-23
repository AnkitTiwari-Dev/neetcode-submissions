class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        nums_set = set(nums)
        max_count = 0
        for num in nums_set:
            counter = 0
            if num - 1 in nums_set:
                continue
            counter += 1
            while num + 1 in nums_set:
                counter += 1
                num = num + 1
            if counter >= max_count:
                max_count = counter
        return max_count
