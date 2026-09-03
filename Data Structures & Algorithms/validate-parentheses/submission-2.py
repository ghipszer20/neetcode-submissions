class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        hshMap = { "}" : "{", "]" : "[", ")" : "(" }

        for char in s:
            if char == "[" or char == "(" or char == "{":
                stack.append(char)
            else:
                if not stack or stack.pop() != hshMap[char]:
                    return False
        
        return not stack
            
                      
        