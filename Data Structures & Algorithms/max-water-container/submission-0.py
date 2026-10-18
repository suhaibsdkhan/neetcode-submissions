class Solution:
    def maxArea(self, heights: List[int]) -> int:
        #the width is the indices (indice2-indice1)
        #the height is the minimum of the two min(height1,height2)
        #multiply the height and width (indice2-indice1) * min (h1,h2)

    # [1,7,2,5,4,7,3,6]
    #  l             r

        maxarea=0

        l,r=0,len(heights)-1
        
        width=r-l
        maxarea=0
        while l<r :
            width=r-l
            newarea=width*min(heights[l],heights[r])
            maxarea=max(maxarea,newarea)

            if heights[l]<heights[r]:
                l+=1
            else:
                r-=1

        return maxarea

