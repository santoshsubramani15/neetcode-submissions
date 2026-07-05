class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        x=[]
        for i in range(len(nums)):
            for j in range(len(nums)):
                if i!=j:
                    a=nums[i]
                    b=nums[j]
                    if a+b==target:
                        p=i
                        q=j
                        if q>p:
                            x.append(p)
                            x.append(q)
                        else:
                            x.append(q)
                            x.append(p)
                        return x
