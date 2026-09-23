class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s)!=len(t):
            return False 
        diction={}
        addiction={}

        for i in range(len(s)):
                if s[i] not in diction:
                    diction[s[i]]=1
                else:
                    diction[s[i]]+=1

        for i in range(len(t)):
                if t[i] not in addiction:
                    addiction[t[i]]=1
                else:
                    addiction[t[i]]+=1

        return diction==addiction
