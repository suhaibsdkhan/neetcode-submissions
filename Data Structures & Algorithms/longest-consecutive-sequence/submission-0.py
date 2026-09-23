class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numSet=set(nums)
        longest=0

        for n in nums:      #for each number in numSet
            if (n-1) not in numSet:     #filters out to get only the starts 
                length=0
                while (n+length) in numSet: 
                    length+=1
                longest=max(length,longest) #keeps track of the longest consecutive group of numbers
        
        
        return longest 
        