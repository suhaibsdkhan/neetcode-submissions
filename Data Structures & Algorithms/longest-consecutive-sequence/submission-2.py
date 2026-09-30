class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        
        numSet=set(nums)
        longest=0
        for i in numSet:
            if (i-1) not in numSet:
                currentlongest=0
                while (i+currentlongest) in numSet:
                    currentlongest+=1
            
                longest=max(currentlongest,longest)


        return longest

        

