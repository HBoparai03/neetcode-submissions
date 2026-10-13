class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        char = {}
        left = 0
        max_freq = 0
        res = 0

        for right in range(len(s)):
            char[s[right]] = 1 + char.get(s[right], 0)
            max_freq = max(max_freq, char[s[right]])

            if (right - left + 1) - max_freq > k:
                char[s[left]] -= 1
                left += 1

            res = max(res, right - left + 1)

        return res
