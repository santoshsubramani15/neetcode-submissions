class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        output=[]
        for i in range(len(nums)):
            product=1
            x=nums.pop(i)
            for j in nums:
                product*= j
            output.append(product)
            nums.insert(i,x)
        return output

        