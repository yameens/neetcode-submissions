class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ## map with sorted as key
        ## combine together after one pass
        from collections import defaultdict

        anagrams = defaultdict(list)
        for word in strs: 
            sorted_str = "".join(sorted(word))
            anagrams[sorted_str].append(word)
        
        result = []
        for word in anagrams.keys():
            result.append(anagrams[word])
        
        return result
        