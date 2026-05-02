class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)

        # iteration over each string
        for s in strs:
            count = [0]*26
            # iteration over each element of the string
            for c in s:
                count[ord(c)-ord('a')] += 1
            # kepping key as a count tuple and value as string
            res[tuple(count)].append(s)
        return list(res.values())