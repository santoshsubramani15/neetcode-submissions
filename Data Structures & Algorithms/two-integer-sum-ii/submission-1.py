class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        a=[]
        x=numbers[:]
        for i in numbers:
            x.remove(i)
            for j in x:
                if i+j==target:
                    a.append(numbers.index(i)+1)
                    a.append(numbers.index(j)+1)
        return a
        