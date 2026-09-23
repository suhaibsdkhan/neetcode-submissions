class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!= len(t):
            return False 

        newdict={}
        newdict2={}

        for i in range(len(s)):
            newdict[s[i]]= 1 + newdict.get(s[i],0)
            newdict2[t[i]]=1 + newdict2.get(t[i],0)

        for j in newdict:
            if newdict[j]!=newdict2.get(j,0):
                return False 

        return True 