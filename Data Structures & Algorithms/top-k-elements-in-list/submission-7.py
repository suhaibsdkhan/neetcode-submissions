class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        #count how many times each number appears

        countdixt={}

        for i in nums:
            countdixt[i]=1+countdixt.get(i,0)

        #make freq,number pairs and sort them, biggest freq first

        newlist=[]

        for n in countdixt:
            newlist.append((countdixt[n],n)) #freq,number pair

        newlist.sort(reverse=True) #sort by freq and reverse to give top first


        #iterate through reversed list and return only the numbers up to k pairs
        finallist=[]
        for i in range(k):
            finallist.append(newlist[i][1])

        return finallist 