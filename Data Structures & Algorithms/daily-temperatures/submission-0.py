class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        outputarray=[0]*len(temperatures)

        stack=[]  #temp and index

        for r in range(len(temperatures)):

            while stack and temperatures[stack[-1]]<temperatures[r]:

                l=stack.pop()

                outputarray[l]=r-l

            stack.append(r)

        return outputarray
        