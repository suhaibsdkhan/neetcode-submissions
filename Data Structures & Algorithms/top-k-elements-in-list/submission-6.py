class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        newdict={}
        finallist=[[] for _ in range(len(nums)+1)]


        for i in range(len(nums)):
            newdict[nums[i]]=1+newdict.get(nums[i],0)

        
        for number,count in newdict.items():
            finallist[count].append(number)
        
        result=[]
        for i in range(len(nums),0,-1):
            for number in finallist[i]:
                result.append(number)
                if len(result)==k:
                    return result 
