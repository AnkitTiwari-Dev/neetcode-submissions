class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new_dict = {}
        for n in nums:
            if n in new_dict:
                new_dict[n] += 1
            else:
                new_dict[n] = 1
        res = sorted(new_dict.keys(), key=lambda x: new_dict[x], reverse=True)
        return res[:k]