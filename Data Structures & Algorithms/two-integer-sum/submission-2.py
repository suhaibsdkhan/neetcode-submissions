class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        new={}      #dictionary of value and the index
        for i,n in enumerate(nums):         #i is the index, n is the value 
            difference= target-n
            if difference in new:
                return [new[difference],i]
            new[n]=i
               
        return 