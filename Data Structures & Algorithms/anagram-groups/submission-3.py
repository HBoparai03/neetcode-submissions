class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        data = defaultdict(list)
        for s in strs:
            temp=[0]*26
            for i in s:
                temp[ord(i)-97] += 1
            temp = tuple(temp)
            data[temp].append(s)
        return list(data.values())

        