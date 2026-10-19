class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketdictionary={")":"(","}":"{","]":"["}

        stack=[]

        for i in s:

            if i in bracketdictionary:

                if stack and stack[-1]==bracketdictionary[i]:
                    stack.pop()
                
                else:
                    return False 

            else:
                stack.append(i)
        
        return True if not stack else False 
        