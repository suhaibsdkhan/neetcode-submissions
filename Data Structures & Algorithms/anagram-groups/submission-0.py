class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #first find the strings that are anagrams of each other 
        #make a new list and include the strings in groups 
        #return the groups 

        anagrams={}

        for word in strs:
            sorted_word=''.join(sorted(word))

            if sorted_word in anagrams:
                anagrams[sorted_word].append(word)
            else:
                anagrams[sorted_word]=[word]


        return list(anagrams.values())