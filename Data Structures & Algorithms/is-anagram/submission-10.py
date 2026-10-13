class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        seenS = {}
        seenT = {}

        for char in s:
            if char in seenS:
                seenS[char] += 1
            else:
                seenS[char] = 1
        for char in t:
            if char in seenT:
                seenT[char] += 1
            else:
                seenT[char] = 1
        if seenS == seenT:
            return True
        else:
            return False
        