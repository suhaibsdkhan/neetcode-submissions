class Solution:
    def isValid(self, s: str) -> bool:
        
        bracketdict={")":"(","]":"[","}":"{"}
        stack=[]

        for i in s:

            if i not in bracketdict:
                stack.append(i)

            else:
                if stack and bracketdict[i]==stack[-1]:
                    stack.pop()
                else:
                    return False 

        return True if not stack else False 