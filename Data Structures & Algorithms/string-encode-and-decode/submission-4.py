class Solution:

    def encode(self, strs: List[str]) -> str:
                #we need length,where it ends/starts

                encoded=[]
                for i in strs:
                    encoded.append(str(len(i)))
                    encoded.append("#")
                    encoded.append(i)

                return "".join(encoded)


    def decode(self, s: str) -> List[str]:

                "5#Hello5#World"
                #  l    r  
                 
                 
                
                decoded=[]

                l=0
                while l<len(s):
                    r=l
                    while s[r]!="#":
                        r+=1
                    length=s[l:r]
                    l=r+1
                    r=l+int(length)
                    string=s[l:r]
                    decoded.append(string)
                    l=r

                return decoded 
                
