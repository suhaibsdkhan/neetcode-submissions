class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        outputarray=[0]*len(temperatures)

        stack=[]

        for i in range(len(temperatures)):

            while stack and temperatures[i]>temperatures[stack[-1]]:
                l=stack.pop()
                outputarray[l]=i-l
                
            stack.append(i)

        return outputarray