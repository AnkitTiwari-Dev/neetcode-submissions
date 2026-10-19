class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        longest = 0
        left = 0
        right = 0
        new_dict = {}
        l = len(s)
        while right < l:
            new_dict[s[right]] = new_dict.get(s[right],0) + 1
            le = right - left + 1
            while le - max(new_dict.values()) > k:
                new_dict[s[left]] -= 1
                left += 1
                le = right - left + 1
            right += 1
            longest = max(longest,le)
        return longest
