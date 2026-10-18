class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        forwards=[]
        backwards=[]

        for i in s:
            if i.isalnum():
                forwards.append(i.lower())

        for j in s[::-1]:
            if j.isalnum():
                backwards.append(j.lower())
        
        return forwards==backwards