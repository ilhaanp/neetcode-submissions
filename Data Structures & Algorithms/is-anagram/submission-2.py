class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        str1 = dict()
        str2 = dict()
        for char in s:
            if char not in str1:
                str1[char] = 0
            str1[char] += 1
        
        for char in t:
            if char not in str2:
                str2[char] = 0
            str2[char] += 1

        return Counter(s) == Counter(t)