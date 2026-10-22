class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        

        result=[1]*len(nums)

        #prefix 

        prefix=1

        for i in range(len(nums)):   #iterate from first to last
            result[i]=prefix
            prefix=prefix*nums[i]


        #suffix

        suffix=1

        for j in range(len(nums)-1,-1,-1): #len(nums)-1 as it is included
                result[j]=result[j]*suffix

                suffix=suffix*nums[j]

        return result 