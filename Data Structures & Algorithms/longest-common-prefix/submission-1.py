class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        x=[]
        y=[]
        for k in range(200):
            x = []
            for i in strs:
                if k >= len(i):
                    return "".join(y)
                a=list(i)
                x.append(a[k])
            c=x.count(x[0])
            if c==len(strs):
                y.append(x[0])
            
            else:
                z=''.join(y)
                return z
        return "".join(y)