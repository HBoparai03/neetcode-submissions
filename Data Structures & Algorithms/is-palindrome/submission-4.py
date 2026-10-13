class Solution:
    def isPalindrome(self, s: str) -> bool:
        t = "".join(x.lower() for x in s if x.isalnum())
        end = len(t) - 1

        for i in range(len(t)):
            if t[i] != t[end]:
                return False
            end -= 1
        return True
        