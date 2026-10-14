class Solution:

    def encode(self, strs: List[str]) -> str:

        encoded=list()

        for i in strs:
            encoded.append(str(len(i)))
            encoded.append("#")
            encoded.append(i)

        return "".join(encoded)

    def decode(self, s: str) -> List[str]:

            decoded=[]

            # 5#Hello5#World 
              #i     j
            i=0

            while i<len(s):

                j=i
                while s[j]!="#":
                    j+=1

                length=s[i:j]
                i=j+1
                j=i+int(length)
                string=s[i:j]
                decoded.append(string)
                i=j
                
            return decoded
                    
                
