class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        charSet=set() #create a set
        l=0           #set left pointer
        maxsize=0       #set variable for maximum size
        for r in range(len(s)):       #iterate right pointer through the string 
            while s[r] in charSet: #while the right character is in the set do the following 
                charSet.remove(s[l])    #remove left character from set
                l+=1        #move left pointer to first character in string now 
            charSet.add(s[r])#add the new right character into the set 
            maxsize=max(maxsize,r-l+1) #set max size 
        return maxsize   #return the max size 