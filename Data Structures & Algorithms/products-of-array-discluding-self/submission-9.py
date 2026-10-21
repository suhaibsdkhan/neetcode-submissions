class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        #[1,1,2,8]
        res=[1]*len(nums)

        prefix=1

        for i in range(len(nums)):
            res[i]=prefix
            prefix*=nums[i]

        suffix=1
        for i in range(len(nums)-1,-1,-1): #(start,stop,interval), stop is -1 to include the first spot

            res[i]*=suffix
            suffix*=nums[i] 

        return res