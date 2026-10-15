class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        seen1 = {}
        seen2 = {}
        left = 0
        right = len(s1) - 1

        for s in s1:
            if s in seen1:
                seen1[s] += 1
            else:
                seen1[s] = 1

        for s in s2[:len(s1)]:
            if s in seen2:
                seen2[s] += 1
            else:
                seen2[s] = 1
        if seen1 == seen2:
            return True
        while right < len(s2)- 1:
            seen2[s2[left]] -= 1
            if seen2[s2[left]] == 0:
                del seen2[s2[left]]
            left += 1
            right += 1
            if s2[right] in seen2:
                seen2[s2[right]] += 1
            else:
                seen2[s2[right]] = 1
            if seen1 == seen2:
                return True
        return False
            

        
        



        