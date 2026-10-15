class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
              #count how many times each number appears
            dict1={}

            for i in nums:
                dict1[i]=1+dict1.get(i,0)



#make freq,number pairs and add into list
            newarray=[]
            
            for value,freq in dict1.items():
                newarray.append([freq,value])


#sort by freq and reverse to give top first, sorts the first item in the list
            newarray.sort(reverse=True)

  #iterate through reversed list and return only the numbers up to k pairs
            finallist=[]

            for i in range(k):
                finallist.append(newarray[i][1])

            return finallist