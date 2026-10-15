class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        current=set(nums)

        longest=0
        for i in nums:
            if (i-1) not in current:
                newlongest=0
                while (i+newlongest) in current:
                    newlongest+=1
                longest=max(longest,newlongest)

        return longest