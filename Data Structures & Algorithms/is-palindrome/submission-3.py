class Solution:
    def isPalindrome(self, s: str) -> bool:
        only_letters = ''.join(c.lower() for c in s if c.isalnum())
        end = len(only_letters) - 1

        for i in range(len(only_letters)):
            if only_letters[i] != only_letters[end]:
                return False
            end -= 1
        return True

