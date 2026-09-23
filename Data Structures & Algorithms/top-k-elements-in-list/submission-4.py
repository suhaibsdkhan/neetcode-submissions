class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        new={}
        newlist=[]
        for i in range(len(nums)):
            new[nums[i]]=1+ new.get(nums[i],0)

        sorted_keys_by_values_desc = sorted(new, key=new.get, reverse=True)
        listt=[]
        for i in range(k):
            listt.append(sorted_keys_by_values_desc[i])
        
        
        return listt