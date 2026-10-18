class Solution:

    def encode(self, strs: List[str]) -> str:
        res = ""
        for s in strs:
            l = len(s)
            res += str(l) + '#' + s
        return res
        
        
    def decode(self, s: str) -> List[str]:
        res = []
        i = 0
        while i < len(s):
            j = i
            while s[j] != '#':
                j += 1
            st = ""
            l = int(s[i:j])
            for k in range(j+1,j + 1 + l):
                st += s[k]
            res.append(st)
            i = j + l + 1
        return res