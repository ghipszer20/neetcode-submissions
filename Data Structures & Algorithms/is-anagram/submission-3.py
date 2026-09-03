class Solution:

    # Two-pointer, sorting approach: O(1) space, O(n + m) time
    def isAnagram(self, s, t):
        s_sorted, t_sorted = sorted(s), sorted(t)
        i, j = 0, 0

        while i < len(s) and j < len(t):
            if s_sorted[i] != t_sorted[j]:
                return False

            i += 1
            j += 1
        
        return i == len(s) and j == len(t)


    # HashMap approach: O(nm) time, O(n + m) space
    # def isAnagram(self, s: str, t: str) -> bool:
    #     hshMap1 = {}
    #     hshMap2 = {}

    #     for letter in s:
    #         if letter not in hshMap1:
    #             hshMap1[letter] = 1
    #         else:
    #             hshMap1[letter] += 1
        
    #     for letter in t:
    #         if letter not in hshMap2:
    #             hshMap2[letter] = 1
    #         else:
    #             hshMap2[letter] += 1
 
    #     for letter in hshMap1:
    #         if letter not in hshMap2 or hshMap2[letter] != hshMap1[letter]:
    #             return False
        
    #     for letter in hshMap2:
    #         if letter not in hshMap1 or hshMap1[letter] != hshMap2[letter]:
    #             return False
            
    #     return True



        