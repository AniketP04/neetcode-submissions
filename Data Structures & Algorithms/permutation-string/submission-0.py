class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        n1, n2 = len(s1), len(s2)

        if n1>n2:
            return False
        
        freq1 = [0]*26
        window = [0]*26

        for ch in s1:
            freq1[ord(ch) - ord('a')] += 1
        
        left = 0

        for right in range(n2):
            window[ord(s2[right]) - ord('a')] += 1

            if right - left + 1 > n1:
                window[ord(s2[left]) - ord('a')] -= 1
                left += 1
            if window == freq1:
                return True
        return False
