class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        x=defaultdict(list)
        for i in strs:
            sortedi=''.join(sorted(i))
            x[sortedi].append(i)
        return list(x.values())

            