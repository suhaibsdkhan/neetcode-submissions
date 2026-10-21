class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        #take the values and put their occurrences in a dictionary

        count={}

        for i in nums:
            count[i]=1+count.get(i,0)

        
        arrayoccurrences=[]

        for value,freq in count.items():

            arrayoccurrences.append([freq,value])       #because freq is what is important 

        arrayoccurrences.sort(reverse=True)
        

        answer=[]
        for i in range(k):
            answer.append(arrayoccurrences[i][1])

        return answer 
