class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq = {}
        for n in nums:
            freq[n] = freq.get(n,0) + 1
        hp = []
        heapq.heapify(hp)
        for key,value in freq.items():
            heapq.heappush(hp,(value,key))
            if len(hp) > k:
                heapq.heappop(hp)
        res = []
        for lst in hp:
            res.append(lst[1])
        return res