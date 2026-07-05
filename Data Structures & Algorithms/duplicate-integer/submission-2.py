class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        c=[]
        for i in nums:
            if i in c:
                return True
                break
            else:
                c.append(i)
        if len(c)==len(nums):
            return False
             
                

                            