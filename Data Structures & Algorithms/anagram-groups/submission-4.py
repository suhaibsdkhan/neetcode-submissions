class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        

        strings=defaultdict(list) #define initial dictionary with listed values

        for s in strs:
            
            key="".join(sorted(s)) #sort to make key

            strings[key].append(s) #add value to key

        return list(strings.values()) #return list of values 