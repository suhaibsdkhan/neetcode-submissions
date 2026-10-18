class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        #sort the input array first
        #[-4,-1,-1-0,1,2]

        sortednums=sorted(nums) #sort input array
        answers=[]              #create a list for the answers
        #iterate the index and value of the sortednums

        for i,v in enumerate(sortednums):
            #if value is the same as the previous index AND (index is greater than 0 ) we skip
            if v==sortednums[i-1] and i>0:
                continue

            #do sorted two integer sum
            p1=i+1
            p2=len(sortednums)-1

            while p1<p2:
                goal= v+sortednums[p1]+sortednums[p2]

                if goal< 0:
                    p1+=1

                elif goal>0:
                    p2-=1

                else:
                    answers.append([v,sortednums[p1],sortednums[p2]])
                     #update pointers as there is more in the sub numbers 
                    p1+=1
                    p2-=1
                    while sortednums[p1]==sortednums[p1-1] and p1<p2:
                        p1+=1

        return answers

     
