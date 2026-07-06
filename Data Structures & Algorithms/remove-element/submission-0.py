class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        c=nums.count(val)
        k=len(nums)-c
        a=nums.copy()
        nums.clear()
        for i in a:
            if i!=val:
                nums.append(i)
        return k 
            
