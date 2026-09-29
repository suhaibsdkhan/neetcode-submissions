class Solution:

    def encode(self, strs: List[str]) -> str:
            
            res=list()

            for i in strs:
                res.append(str(len(i)))
               
                res.append("#")
                res.append(i)
            return "".join(res)

    def decode(self, s: str) -> List[str]:

            res=[]
           # "5#Hello5#World"
            #        j  
                     #i

            i=0

            while i<len(s):
                
                j=i
                while s[j]!="#":
                    j+=1
                length=s[i:j]
                i=j+1
                j=i+int(length)
                res.append(s[i:j])
                i=j
                
            return res


                







