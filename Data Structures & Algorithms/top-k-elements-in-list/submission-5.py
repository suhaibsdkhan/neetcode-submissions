class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new={}
        listy=[[]for i in range(len(nums)+1)]

        for i in nums:
            new[i]=1+new.get(i,0)

        for i,c in new.items():
            listy[c].append(i)

        res=[]

        for m in range(len(listy)-1,0,-1):
            for i in listy[m]:
                res.append(i)
                if len(res)==k:
                    return res