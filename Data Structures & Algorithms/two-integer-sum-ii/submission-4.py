class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        length=len(numbers)
        pointer1=0
        pointer2=length-1

        goal=numbers[pointer1]+numbers[pointer2]

        while goal!=target:

            if goal>target:
                pointer2-=1

            elif goal<target:
                pointer1+=1

            goal=numbers[pointer1]+numbers[pointer2]

        return [pointer1+1,pointer2+1]