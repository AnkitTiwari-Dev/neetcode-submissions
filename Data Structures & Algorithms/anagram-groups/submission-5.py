class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        new_dict = {}
        for s in strs:
            count = [0] * 26
            for c in s:
                idx = ord(c) - ord('a')
                count[idx] += 1
            key = tuple(count)
            if key not in new_dict:
                new_dict[key] = []
            new_dict[key].append(s)
        return list(new_dict.values())