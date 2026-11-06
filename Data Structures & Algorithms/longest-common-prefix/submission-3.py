class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        for i in range(len(strs[0])):
            for j in strs[1:]:
                if len(j) <= i or j[i] != strs[0][i]:
                    return strs[0][:i]
        return strs[0]