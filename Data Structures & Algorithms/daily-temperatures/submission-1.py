class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res = []

        for i in range(len(temperatures)):
            count = 0
            found = False
            for j in range(i + 1, len(temperatures)):
                if temperatures[j] > temperatures[i]:
                    count = j - i
                    found = True
                    break
            if found:
                res.append(count)
            else:
                res.append(0)
        return res

        