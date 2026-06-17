class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        sLetters = []
        tLetters = []
        for i in s:
            sLetters.append(i)
        for j in t:
            tLetters.append(j)
        newS= sorted(sLetters)
        newT= sorted(tLetters)
        return newS == newT
        
        