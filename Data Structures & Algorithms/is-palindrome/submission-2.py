class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = ''.join(c.lower() for c in s if c.isalnum())

        i = 0
        k = len(only_letters) - 1

        while i < k:
            if only_letters[i] != only_letters[k]:
                return False
            i += 1
            k -= 1

        return True
