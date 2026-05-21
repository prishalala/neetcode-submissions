class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        count = 0
        for i in range(len(s)):
            s1 = set()
            for j in range(i, len(s)):
                if s[j] in s1:
                    break
                s1.add(s[j])
            count = max(count, len(s1))
        return count