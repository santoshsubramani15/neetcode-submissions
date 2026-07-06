class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        x = {}
        # Count frequencies
        for i in set(nums):
            x[i] = nums.count(i)
        
        # Sort the dictionary items by frequency (value) in descending order
        # x.items() gives (number, frequency). item[1] is the frequency.
        sorted_items = sorted(x.items(), key=lambda item: item[1], reverse=True)
        
        # Grab the first k numbers from the sorted list
        a = []
        for j in range(k):
            a.append(sorted_items[j][0])
            
        return a
        