class Solution:

    def encode(self, strs: List[str]) -> str:

            if strs == None :
                return None
            
            encoded_string=''
            for i in range(len(strs)):
                encoded_string+= str(len(strs[i]))+"#"+strs[i]
            
            return encoded_string
            
    def decode(self, s: str) -> List[str]:

            if s == None:
                return None 
            new_array=[]
            
            i=0
            while i < len(s):
            #find the position on # with j as # pointer and i as #number pointer
                 j = i
                 while s[j] != '#':
                     j += 1
            # find length using i and j

                 length = int(s[i:j])

            # use j to find bounds of string and add into new_array 

                 new_array.append(s[j + 1:j + 1 + length])

            # Move to the next encoded string
            #reset i position to the number(length) of next string 
                 i = j + 1 + length

            return new_array
