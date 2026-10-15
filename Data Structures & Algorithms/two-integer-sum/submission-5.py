class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        
        newdict={}

        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in newdict:
                return [newdict[diff],i]

            newdict[nums[i]]=i

        
