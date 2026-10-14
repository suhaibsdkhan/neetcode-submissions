class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        new=defaultdict(list)

        for i in strs:
            key="".join(sorted(i))
            new[key].append(i)

        return list(new.values())