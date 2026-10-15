class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        
        n=len(numbers)
        #if the target is greater
        pointer1=0
        pointer2=n-1
        reach=numbers[pointer1]+numbers[pointer2]

        while reach!=target:
            
            if reach>target: 
                pointer2-=1
            else:
                pointer1+=1

            reach=numbers[pointer1]+numbers[pointer2]
        
        return [pointer1+1,pointer2+1]


        