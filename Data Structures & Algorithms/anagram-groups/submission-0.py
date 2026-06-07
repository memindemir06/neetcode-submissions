class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        group = {}
        
        for string in strs:
            freq = [0] * 26
            for char in string:
                freq[ord(char) - 97] += 1
            freq_key = str(freq)
            if freq_key in group:
                group[freq_key].append(string)
            else:
                group[freq_key] = [string]

        return [i for i in group.values()]
