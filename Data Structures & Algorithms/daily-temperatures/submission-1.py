class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        outputarray=[0]*len(temperatures)       #initialize with 0, counts for the last ones that dont have any temp higher than them

        stack=[]  #indices of days waiting for a warmer day

        for r in range(len(temperatures)): #r=today

            while stack and temperatures[r]>temperatures[stack[-1]]: #today is warmer than top day?
                l=stack.pop()           #today is warmer than day on top of stack

                outputarray[l]=r-l      #set the days it waited

            stack.append(r)        #today starts waiting 

        return outputarray          #leftover days stay 0
        