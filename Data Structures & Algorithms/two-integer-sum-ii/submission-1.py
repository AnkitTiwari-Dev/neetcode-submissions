class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left = 0
        right = len(numbers)
        while left < right:
            res = numbers[left] + numbers[right - 1]
            if res == target:
                return [left + 1,right]
            if res < target:
                left += 1
            else:
                right -= 1
            