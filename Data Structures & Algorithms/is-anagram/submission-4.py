class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        l1=list(s)
        l2=list(t)
        for i in list(l1):
            if i in l2:
                l1.remove(i)
                l2.remove(i)
        if l2==[] and l1==[]:
            return True
        else:
            return False
