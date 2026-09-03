class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        hshMap1 = {}
        hshMap2 = {}

        for letter in s:
            if letter not in hshMap1:
                hshMap1[letter] = 1
            else:
                hshMap1[letter] += 1
        
        for letter in t:
            if letter not in hshMap2:
                hshMap2[letter] = 1
            else:
                hshMap2[letter] += 1
        
        for letter in hshMap1:
            if letter not in hshMap2 or hshMap2[letter] != hshMap1[letter]:
                return False
        
        for letter in hshMap2:
            if letter not in hshMap1 or hshMap1[letter] != hshMap2[letter]:
                return False
            
        return True



        